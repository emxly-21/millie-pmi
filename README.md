# millie-pmi
## Overview
A Proactive Mentor Intaker (PMI) for Millie's Tech & Product Internship. Running `main.py` creates a Tkinter GUI to take in and store information, which is then used to access and scrape a LinkedIn profile for data using Selenium.

## Required Installations
Make sure you have Python 3 and Google Chrome installed. Also please install Selenium (`pip install selenium`) and ChromeDriver (see [this page](https://sites.google.com/a/chromium.org/chromedriver/downloads) for installation instructions).

## Setup
1. Clone this repository by typing `git clone https://github.com/emxly-21/millie-pmi.git` into your terminal.
2. Open the `credentials.py` file, and enter your LinkedIn user ID and password.
3. Navigate to where you downloaded ChromeDriver, and copy the path. Paste that into `linkedin-login.py` where the code says `driver = webdriver.Chrome('<INSERT PATH TO CHROMEDRIVER>')`.
4. Run `linkedin-login.py`. A dummy Chrome browser should open and log you into LinkedIn.
    * If you have two-factor authentication via SMS enabled, enter your verification code into your IDE when prompted, NOT in the browser (as you would when you normally log in). This code cannot yet handle two-factor authentication using an authenticator app.
    * After successfully logging in to LinkedIn, a new file called `session.txt` will be created. Do NOT close the dummy Chrome browser, or you will need to run `linkedin-login.py` again.
  
## Running
Run `main.py` either in an IDE or by typing `python3 main.py` into your terminal. A window should pop up, where the user can type in information about them, including a link to their LinkedIn profile. Once the user clicks submit, this window will close, and the information will be saved to a file called `lastStored.txt`. The program will then begin searching the user's LinkedIn profile.

Upon completion, the program will print out a summary of the information found in the Education section of the user's LinkedIn, as well as several variables (including name, university, graduation year, etc.). These variables will then be saved to a CSV database, `database.csv`.
