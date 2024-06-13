pip install --no-input flask 
pip install --no-input selenium
pip install --no-input -U pyvo
curl https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.55/mac-arm64/chromedriver-mac-arm64.zip 

dir=$(pwd)
echo -e "#!/bin/bash\npython $dir/app.py" >> macexec.command
chmod u+x macexec.command
cp macexec.command ~/Desktop

echo
echo -------------------------
echo !!INSTALLATION COMPLETE!!
echo -------------------------
echo

