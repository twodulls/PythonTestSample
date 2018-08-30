'''
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.FIREFOX

# Tell the Python bindings to use Marionette.
# This will not be necessary in the future,
# when Selenium will auto-detect what remote end
# it is talking to.
caps["marionette"] = True

# Path to Firefox DevEdition or Nightly.
# Firefox 47 (stable) is currently not supported,
# and may give you a suboptimal experience.
#
# On Mac OS you must point to the binary executable
# inside the application package, such as
# /Applications/FirefoxNightly.app/Contents/MacOS/firefox-bin
caps["binary"] = "C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
geckodriver="D:\workspace_python\selenium_test\webdriver_server\geckodriver.exe"

driver = webdriver.Firefox(capabilities=caps, executable_path="D:\workspace_python\selenium_test\webdriver_server\geckodriver.exe")
driver.get("http://www.google.com")
print(driver.title)
driver.quit()
'''

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps=DesiredCapabilities.FIREFOX
caps["marionette"]=True
driver=webdriver.Firefox(capabilities=caps, executable_path="D:\selenium-webdriver\geckodriver.exe")
driver.get("http://www.ticketmonster.co.kr")
print(driver.title)

driver.quit()