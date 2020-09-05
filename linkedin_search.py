from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import re

CURR_YR = 2020
international = ["International Baccalaureate", "IBDP", "IB Score", "A Level", "French Baccalaureate"]

# reattaches the Web Driver so that the user does not need to log in again
# code from Stack Overflow
# https://tarunlalwani.com/post/reusing-existing-browser-session-selenium/
def attach_to_session(executor_url, session_id):
    original_execute = WebDriver.execute
    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return original_execute(self, command, params)
    # Patch the function before creating the driver object
    WebDriver.execute = new_command_execute
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    driver.session_id = session_id
    # Replace the patched function with original function
    WebDriver.execute = original_execute
    return driver

def search(url):
    f = open("session.txt", "r")
    executor = f.readline().strip('\n')
    session_id = f.readline()
    f.close()

    driver = attach_to_session(executor, session_id)

    # goes to the LinkedIn profile to be searched
    driver.get(url)

    university = ''
    grad_yr = ''
    yrs_experience = 0
    high_school = 'N'
    last_grad = 0

    html = driver.page_source

    education = [m.start() for m in re.finditer('com.linkedin.voyager.dash.deco.identity.profile.FullProfileEducation"]', html)]
    education.insert(0, 0)
    education.append(len(html))

    for x in range(1, len(education)-1):
        start = html.rindex('{"dateRange":{', education[x-1], education[x])
        end = education[x+1]

        degree_start = html.index('"degreeName":', start, end)
        if html[degree_start+13:degree_start+17] == "null":
            degree_name = "N/A"
        else:
            degree_name = html[degree_start+14:html.index('",', degree_start, end)]

        if '"end":{"year":' in html[start:end]:
            grad_start = html.index('"end":{"year":', start, end)
            grad = int(html[grad_start+14:html.index(',"', grad_start, end)])
        elif '"end":{"month":' in html[start:end]:
            grad_start = html.index('"year":', html.index('"end":{"month"'), end)
            grad = int(html[grad_start+7:html.index(',"', grad_start, end)])

        school_start = html.index('"schoolName":', start, end)
        school_name = html[school_start+14:html.index('",', school_start, end)]

        print(", ".join([school_name, degree_name, str(grad)]))
        print()

        if "Bachelor" in degree_name:
            university = school_name
            grad_yr = grad

        if grad > last_grad and grad <= CURR_YR:
            last_grad = grad

        if "High School" in school_name or "High School" in degree_name:
            if any(element in html[start:end] for element in international):
                high_school = 'Y'

    if last_grad > 0:
        yrs_experience = CURR_YR - last_grad

    print("University:\t\t\t\t\t", university)
    print("Undergrad Graduation Year:\t", grad_yr)
    print("Years of Experience:\t\t", str(yrs_experience))
    print("International High School?\t", high_school)

    return university, grad_yr, yrs_experience, high_school
