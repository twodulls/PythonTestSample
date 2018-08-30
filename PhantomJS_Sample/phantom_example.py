from selenium import webdriver

#executable_path 항목의 경로부분 앞에 꼭 r을 추가해야 한다.
driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get("http://www.naver.com")
print(driver.title)
driver.quit()