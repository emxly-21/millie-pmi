# millie-pmi
## Required Installations
Make sure you have Python 3 and Google Chrome installed. Also please install Selenium (`pip install selenium`) and ChromeDriver (see [this page](https://sites.google.com/a/chromium.org/chromedriver/downloads) for installation instructions).

## Setup
1. Clone this repository by typing `git clone https://github.com/emxly-21/millie-pmi.git` into your terminal.
2. Open the `credentials.py` file, and enter your LinkedIn user ID and password.
3. Navigate to where you downloaded ChromeDriver, and copy the path. Paste that into `linkedin-login.py` where the code says `driver = webdriver.Chrome('<PATH TO CHROMEDRIVER>')`.
4. Run `linkedin-login.py`. A dummy Chrome browser should open and log you into LinkedIn. Currently, the code is written to handle two-factor authentication via SMS. When you receive your verification code, enter it in your IDE, NOT in the browser. You should now be successfully logged in to LinkedIn. Do NOT close the dummy Chrome browser.
