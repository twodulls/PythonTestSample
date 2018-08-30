from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.INTERNETEXPLORER
caps['ignoreProtectedModeSettings'] = True

binary = 'D:\workspace_python\selenium_test\webdriver_server\IEDriverServer.exe'
driver = webdriver.Ie(binary, capabilities=caps)
driver.implicitly_wait(10)
driver.get("http://www.ticketmonster.co.kr/home")

print(driver.title)
driver.quit()
