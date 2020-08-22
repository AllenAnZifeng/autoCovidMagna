import time
from config import ChromeDriverPath, INFORMATION, EMAIL, PASSWORD

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print(INFORMATION)

def clickRadioButton():
    clickButton('input[value="437470001"]')
    clickButton('input[value="Next"]')

def validateLoading(cssSelector):
    try:
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, cssSelector))
        )
    except Exception as e:
        print(e)


def clickButton(cssSelector):
    time.sleep(0.5)
    validateLoading(cssSelector)
    driver.find_element_by_css_selector(cssSelector).click()

def sendkeys(cssSelector,msg):
    time.sleep(0.5)
    validateLoading(cssSelector)
    driver.find_element_by_css_selector(cssSelector).send_keys(msg)

def sendMail(url):
    subject = "Magna健康表单填写确认"
    body = str(url)
    sender_email = EMAIL
    receiver_email = INFORMATION['email']
    password = PASSWORD

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # filename = "document.pdf"
    #
    # # Open PDF file in binary mode
    # with open(filename, "rb") as attachment:
    #     # Add file as application/octet-stream
    #     # Email client can usually download this automatically as attachment
    #     part = MIMEBase("application", "octet-stream")
    #     part.set_payload(attachment.read())
    #
    # # Encode file in ASCII characters to send by email
    # encoders.encode_base64(part)
    #
    # # Add header as key/value pair to attachment part
    # part.add_header(
    #     "Content-Disposition",
    #     f"attachment; filename= {filename}",
    # )
    #
    # # Add attachment to message and convert message to string
    # message.attach(part)

    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


driver = webdriver.Chrome(ChromeDriverPath)  # Optional argument, if not specified will search path.
driver.get('https://magnascreening.powerappsportals.com/en-US/?country=Canada&division=Precision%20Technologies')


clickButton('div a.btn')

clickButton('table [data-name="Country"] .launchentitylookup')
clickButton('tr [data-id="d6676e7b-7977-ea11-a811-000d3af42c56"]')
clickButton('table [data-name="Country"] div.modal-footer [title="Select"]')

clickButton('table [data-name="DivisionSection"] .launchentitylookup')

sendkeys('input.query','precision')
# driver.find_element_by_css_selector('input.query').send_keys('precision')

clickButton('button[title="Search Results"]')
clickButton('table [data-name="DivisionSection"] div.modal-footer [title="Select"]')
clickButton('div [role="group"] input')

sendkeys('input[title="Please enter your fist name"]',INFORMATION['firstname'])
sendkeys('input[title="Please enter your last name"]',INFORMATION['lastname'])
sendkeys('input[title="Please enter your phone number"]',INFORMATION['phone'])

clickButton('div.actions input[value="Next"]')

clickButton('input[value="437470008"]')
clickButton('input[value="Next"]')

for i in range(3):
    clickRadioButton()


# # driver.save_screenshot('covid_check.png')
# driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')

# message to be sent
message = driver.current_url

print(message)
sendMail(message)

driver.quit()
