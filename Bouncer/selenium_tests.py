import unittest, sys, re, time
from settings import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import sys

desired_drivers = []
if sys.platform == 'linux2':
	desired_drivers.append("webdriver.Chrome('/usr/bin/chromedriver')")
	# desired_drivers.append("webdriver.Firefox(firefox_binary=binary)")

elif sys.platform == 'win32':
	desired_drivers.append("webdriver.Chrome('../selenium_browser_drivers/chromedriver.exe')")
	desired_drivers.append("webdriver.Firefox()")

class current_test_case(unittest.TestCase):

	#unittest will automatically call set_up and then tear_down, these two functions comprise the testing fixture

	def setUp(self):
		for driver_instance in desired_drivers:

			self.driver = eval(driver_instance)

	def tearDown(self):
		self.driver.quit()
		print("quit " + str(self.driver) )

	def testLogUpload(self):
		self.driver.get('http://127.0.0.1:8000/simple')
		file_path = BASE_DIR + '/testlog.txt'

		element = self.driver.find_element_by_id('myfile')
		element.send_keys(file_path)
		element.submit()
		time.sleep(1)
		element = self.driver.find_element_by_id('post_msg')
		regex = 'File \w+\.txt uploaded'
		self.assertTrue(re.match(regex, element.text))

if __name__ == '__main__':
    unittest.main()
