from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


caps= {
    "platformName":"Android",
    "deviceName": "emulator-5554",
    "app": 'C:\\Users\\Murali Krishna\Documents\\LR\\appium\\exp\\Theapp.apk'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

driver.find_element(MobileBy.CLASS_NAME, "android.widget.TextView")
driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='Webview Demo']")

WebDriverWait(driver, 1000)
"""
try:
    wait = WebDriverWait(driver, 10)
    wait.until(ec.p)

finally:
"""
driver.quit()
#driver.get('http://google.com')
