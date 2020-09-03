# millie-pmi
## Required Installations
Make sure you have Python 3 and Google Chrome installed. Also please install Selenium (`pip install selenium`) and ChromeDriver (see [this page](https://sites.google.com/a/chromium.org/chromedriver/downloads) for installation instructions).

## Setup
1. Clone this repository by typing `git clone https://github.com/emxly-21/millie-pmi.git` into your terminal.
2. Open the `credentials.py` file, and enter your LinkedIn user ID and password.
3. Navigate to where you downloaded ChromeDriver, and copy the path. Paste that into `linkedin-login.py` where the code says `driver = webdriver.Chrome('<INSERT PATH TO CHROMEDRIVER>')`.
4. Run `linkedin-login.py`. A dummy Chrome browser should open and log you into LinkedIn. If you have two-factor authentication via SMS enabled, enter your verification code into your IDE when prompted, NOT in the browser (as you would when you normally log in). This code cannot yet handle two-factor authentication using an authenticator app. After successfully logging in to LinkedIn, do NOT close the dummy Chrome browser.
