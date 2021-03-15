from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# reads input from console
usernameStr = str(input("putYourUsernameHere: "))
passwordStr = str(input("putYourPasswordHere: "))


def bot(usr, pas):
    # Finds driver in your file system... must have chrome installed. If file doesn't exist, the driver will be auto downloaded.
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Brockport url
    browser.get("https://www.brockport.edu/bounce/medicat")

    # user name enter box html id
    username = browser.find_element_by_id("username")
    browser.implicitly_wait(10)
    # enters parameter usr into username text box on website
    username.send_keys(usr)

    # password enter box html id
    password = browser.find_element_by_id("password")
    browser.implicitly_wait(10)
    # enters parameter pas into password text box on website
    password.send_keys(pas)

    # uses the xpath of the submit username and password button
    sign_in_button = browser.find_element_by_css_selector("button[class='wr-btn grey-bg col-xs-12 col-md-12 col-lg-12 uppercase font-extra-large margin-bottom-double']")
    sign_in_button.click()

    # uses the xpath for covid task bar
    covid_link = browser.find_element_by_xpath("//*[@id='ctl00_navBar_liStatus']/a")
    covid_link.click()

    # uses xpath for covid tracker link on webpage
    symptoms_tracker = browser.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_divForms']/div/div/div/h4/a")
    symptoms_tracker.click()

    # xpath for first radio button (question 1)
    radio_button_1 = browser.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_RadioGroup61514_1']")
    radio_button_1.click()

    # xpath for second radio button (question 2)
    radio_button_2 = browser.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_RadioGroup61421_1']")
    radio_button_2.click()

    # xpath for submit survey button
    submit_survey = browser.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_lbtnSubmit']")
    submit_survey.click()



bot(usernameStr, passwordStr)
