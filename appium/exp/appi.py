from appium import webdriver
from os import path

#CUR_DIR = path.dirname(path.abspath(__file__)) 
#APP = path.join(CUR_DIR, 'TheApp.apk')
APPIUM = 'http://localhost:4723/'
CAPS = {
    'platformName' : 'Android',
    'platformVersion' : '11.0',
    'deviceName' : 'emulator-5554',
    'automationName' : 'UiAutomator2',
    'browserName': 'Chrome'
    #'app': APP, 
}

driver = webdriver.Remote(APPIUM, CAPS)
driver.quit()
