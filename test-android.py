from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {
    "deviceName": "Android Emulator",
    "platformName": "Android",
    "app": "C:\\Users\\Shivani Desai\\Downloads\\Handyman App Demo for Testing by Call4site com_v1.0_apkpure.com.apk",
    "appPackage": "com.call4site.handymanservices",
    "appWaitActivity": "com.call4site.handymanservices.activity.LoginActivity"
}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=desired_caps)
wait = WebDriverWait(driver, 10)

wait.until(EC.visibility_of_element_located((By.ID, "com.call4site.handymanservices:id/email")))

driver.find_element_by_id("com.call4site.handymanservices:id/email").send_keys("testing@gmail.com")

driver.find_element_by_id("com.call4site.handymanservices:id/password").send_keys("checking")

buttn = driver.find_element_by_class_name("android.widget.Button")

driver.set_value(buttn, 'SIGN IN' )
#driver.implicitly_wait(10)

