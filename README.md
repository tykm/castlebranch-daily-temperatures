This is my script to automate my 2x per day temperature check-in at CastleBranch.

Requirements:
pip  
`https://pip.pypa.io/en/stable/installing/`  
selenium  
`pip install -U selenium`  
chromedriver  
`https://chromedriver.chromium.org/downloads`  
python-dotenv  
`pip install python-dotenv`  

Setup:
1. Create a .env file following the .env.example format
2. For mac users, put chromedriver in `usr/local/bin`. For windows, specify chromedriver location in PATH.

Troubleshooting:
Chromedriver will not run because unidentified developer
`https://support.apple.com/guide/mac-help/open-a-mac-app-from-an-unidentified-developer-mh40616/mac`


Resources:
Controlling the web with python - https://towardsdatascience.com/controlling-the-web-with-python-6fceb22c5f08
Locating elements with selenium - https://selenium-python.readthedocs.io/locating-elements.html
Explicit wait - https://www.selenium.dev/documentation/en/webdriver/waits/