# Test keywords

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

class keywords(object):

	def __init__(self):
		pass
		
	def ML_get_page(self, wd, assertItem):
		print ('----- ML_get_page ----')
		self.wd.get("http://en.wikipedia.org/wiki/Wikipedia") # Load page
		assert "Wikipedia" in self.wd.title
		elem = self.wd.find_element_by_id('searchInput') # Find the query box
		elem.send_keys("selenium" + Keys.RETURN)
		time.sleep(0.2) # Let the page load, will be added to the API
		try:
			self.wd.find_element_by_xpath("//a[contains(@id,assertItem)]")
		except NoSuchElementException:
			assert 0, "can't find element - Top"
		
		self._capture_screenshot()
		
	def _helper_capture_screenshot(self):
		self.wd.save_screenshot('ScreenShot.png')
	
	