import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

desired_drivers = []
desired_drivers.append("webdriver.Chrome('/usr/bin/chromedriver')")
# desired_drivers.append("webdriver.Firefox('/usr/bin/geckodriver')")


class current_test_case(unittest.TestCase):

	#unittest will automatically call set_up and then tear_down, these two functions comprise the testing fixture

	def setUp(self):
		for driver_instance in desired_drivers:
			if driver_instance == "webdriver.Firefox(firefox_binary=binary)":
				binary = FirefoxBinary(r'../selenium_browser_drivers/geckodriver-v0.15.0-win64/geckodriver.exe')

			self.driver = eval(driver_instance)



	def tearDown(self):
		self.driver.quit()
		print("quit " + str(self.driver) )


	def testExample(self):
		self.driver.get("http://www.google.com/")
		print("got the googs\n")
		print(self.driver.title)

	def testLogUpload(self):

		self.driver.get('http://127.0.0.1:8000/simple')
		file_path = '../testlog.txt'
		element = self.driver.find_element_by_id('myfile')
		element.send_keys(file_path)

		# validate...


if __name__ == '__main__':
    unittest.main()

