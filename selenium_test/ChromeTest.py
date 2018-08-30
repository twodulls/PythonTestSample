import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ChromeTest(unittest.TestCase):
	
	def setUp(self):
		binary = 'D:\workspace_python\selenium_test\webdriver_server\chromedriver.exe'
		self.driver = webdriver.Chrome(binary)

	def test_search_in_python_org(self):
		driver = self.driver
		driver.get('http://www.python.org')
		self.assertIn("Python", driver.title)

		elem = driver.find_element_by_name("q")
		elem.send_keys("pycon")
		elem.send_keys(Keys.RETURN)

		assert "No results found." not in driver.page_source

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
    unittest.main()