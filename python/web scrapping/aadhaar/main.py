
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request

def create_driver():
    # create webdriver object
    driver = webdriver.Chrome()
    driver.get("https://myaadhaar.uidai.gov.in/genricDownloadAadhaar")

    aadhaarno = driver.find_element(By.NAME, "uid")
    print(aadhaarno.text)
    aadhaarno.send_keys("30200")

    cap = driver.find_element(By.CLASS_NAME, "auth-form__captcha-image")
    # with open('Logo.png', 'wb') as file:

    #     l = driver.find_element(By.CLASS_NAME, "auth-form__captcha-image")
    #     file.write(l.screenshot_as_png)
    urllib.request.urlretrieve(cap.get_attribute('src'), "captcha.png")



