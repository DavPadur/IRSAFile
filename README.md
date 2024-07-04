### Step 1: Install the file

Click the green "Code" button and download the .zip file to your systems desktop

![check_install_to_path](https://i.imgur.com/hXqWWJP.png)

![check_install_to_path](https://i.imgur.com/HihRwsu.png)

From your desktop then extract it back again to your desktop.

### Step 2: Install Python

Make sure Python is installed on your system. You can download and install Python from [python.org](https://www.python.org/downloads/). 

 (DOWNLOAD THE LATEST VERSION AND CLICK THE BOX AT THE BOTTOM OF THE INSTALLER TO INSTALL TO PATH)

![check_install_to_path](https://i.imgur.com/Cw5ziwU.png)

### Step 3: Install Dependencies

Install the required dependencies by copy and pasting the command below into your respective terminal. (mac: terminal / windows: command prompt)

   ```Windows
   pip install -U pyvo selenium flask
   ```

   ```Mac
   pip3 install -U pyvo selenium flask
   ```

### Step 4: Install ChromeDriver 

Paste the following link into your web browser, and install into the FlaskApp folder

Windows:
   https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/win64/chromedriver-win64.zip

Mac (M1+):
   https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/mac-arm64/chromedriver-mac-arm64.zip

Mac (Intel):
   https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/mac-x64/chromedriver-mac-x64.zip

### Step 5: Extract the .zip file

Once you have extracted the files, install chrome driver by entering the extracted file 

![check_install_to_path](https://i.imgur.com/oqqRTyc.png)

Then clicking on chromedriver

![check_install_to_path](https://i.imgur.com/IvxsKna.png)

### Step 6: Running the Program

Now click on your systems respective exec command (winexec/macexec)

Then enter the URL: http://127.0.0.1:5001/

### Step 7: GOOD JOB

Navigate to the respective tab of what you would like to do, Query to find the star position in the database or IRSA to open that new .tbl file in the IRSA viewer

Every time now after, all you have to do is repeat Step 6


---

## Extra Instructions 

### Running your Flask App

1 - git clone the repository into VS Code / IDE (look up on Google or ask chatGPT how to do it if you don't know).

2 - Open terminal in VS CODE / IDE, ensure your terminal path is in the folder "FlaskApp" where the app.py script is located so IRSAFILE/FlaskApp

3 - Run the next commands
 
``` set FLASK_APP=app.py ``` 

```flask run --host=127.0.0.1 --port=5001```

4 - Now your app should be running and you should see the following on the terminal
``` 
 * Running on http://127.0.0.1:5001
 ```
