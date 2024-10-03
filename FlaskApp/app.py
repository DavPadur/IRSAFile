from flask import Flask, request, render_template, flash
from werkzeug.utils import secure_filename
import pyvo
from astropy.io import ascii
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
from sys import platform
import chromedriver_autoinstaller

if platform != 'win32':
    file_dir = os.path.join(os.path.expanduser('~'), 'Desktop/IRSAFile-main/FlaskApp/')
else:
    file_dir = os.path.join(os.environ['USERPROFILE'], 'Desktop\\IRSAFile-main\\IRSAFile-main\\FlaskApp\\')

driver_path = chromedriver_autoinstaller.install()

app = Flask(__name__)
app.secret_key = 'IRSA_secret_key'  

ALLOWED_EXTENSIONS = {'tbl'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/query", methods=['POST', 'GET'])
def query():
    service = pyvo.dal.TAPService('https://irsa.ipac.caltech.edu/TAP')

    def fetch_neowise_data(ra, dec, filename):
        query = f"""
            SELECT ra, dec, mjd, w1mpro, w1sigmpro, w2mpro, w2sigmpro, source_id, frame_num, scan_id
            FROM neowiser_p1bs_psd
            WHERE CONTAINS(POINT('J2000', ra, dec), CIRCLE('J2000', {ra}, {dec}, 0.0002777777778))=1
        """
        result = service.run_async(query)
        tab = result.to_table()
        ascii.write(tab, os.path.join(file_dir, f'{filename}.tbl'), format='ipac', overwrite=True)

    if request.method == 'POST':
            ra = request.form.get('ra')
            dec = request.form.get('dec')
            filename = request.form.get('filename')

            if not ra or not dec or not filename:
                flash('Please provide valid RA, DEC, and Filename values.', 'warning')
            else:
                try:
                    fetch_neowise_data(ra, dec, filename)
                    flash('File has been saved successfully!', 'success')
                except Exception as e:
                    flash(f'An error occurred: {e}', 'error')
    
    return render_template("query.html")

@app.route("/irsa", methods=['GET', 'POST'])
def irsa():
    def upload_file(driver, wait, file_path):
        try:
            if not os.path.exists(file_path):
                print(f"File not found: {file_path}")
                return

            print(f"Uploading file: {file_path}")

            file_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
            file_input.send_keys(file_path)
            print(f"File path sent to input field: {file_path}")

            upload_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Upload")]')))
            upload_button.click()

            click_bottom_left_upload(wait)
            print(f"File uploaded: {file_path}")

        except Exception as e:
            print(f"An error occurred while uploading file {file_path}: {e}")

    def click_bottom_left_upload(wait):
        try:
            xpath = '//button[contains(text(), "Upload") and contains(@class, "MuiButton-root")]'
            bottom_left_upload_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            bottom_left_upload_button.click()
        except Exception as e:
            print(f"An error occurred while clicking the bottom left upload button: {e}")
    if request.method == 'POST':
        uploaded_file_paths = []

        if 'files' in request.files:
            files = request.files.getlist('files')
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(file_dir, filename)
                    file.save(file_path)
                    uploaded_file_paths.append(file_path)

        if 'filenames' in request.form and request.form['filenames']:
            filenames = request.form['filenames'].split(',')
            for filename in filenames:
                file_path = os.path.join(file_dir, f'{filename.strip()}.tbl')
                if os.path.exists(file_path):
                    uploaded_file_paths.append(file_path)
                else:
                    flash(f'File not found: {file_path}', 'error')

        if uploaded_file_paths:
            chrome_service = Service(driver_path)
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)

            if platform != 'win32':
                chrome_binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
                chrome_options.binary_location = chrome_binary_location

            driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
            driver.get('https://irsa.ipac.caltech.edu/irsaviewer/timeseries?__action=layout.showDropDown&')
            wait = WebDriverWait(driver, 10)

            upload_file(driver, wait, uploaded_file_paths[0])

            for file_path in uploaded_file_paths[1:]:
                driver.execute_script("window.open('about:blank', '_blank');")
                driver.switch_to.window(driver.window_handles[-1])
                driver.get('https://irsa.ipac.caltech.edu/irsaviewer/timeseries?__action=layout.showDropDown&')
                upload_file(driver, wait, file_path)

            driver.switch_to.window(driver.window_handles[0])
            is_seen_items_present = driver.execute_script("return localStorage.getItem('seenItems') !== null;")
            print(f"LocalStorage 'seenItems' presence: {is_seen_items_present}")

        else:
            flash('No valid files uploaded.', 'error')

    return render_template("irsa.html")


if __name__ == '__main__':
    app.run(debug=True, port=5001)
