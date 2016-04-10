from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time
from testsetup  import TestSetUp

class SearchActions(unittest.TestCase):
      def test_SearchActions(self):
          obj = TestSetUp(webdriver.Chrome())
          obj.setUp()
          helpcenterMenuLocator = "/html/body/div[1]/nav/div/div[1]/div[2]/ul/li[3]/a"
          searchMenuLocator = "//input[@class='search-input']"
          helpcenterElement = WebDriverWait(obj.driver, 10).\
                              until(lambda driver:(obj.driver).find_element_by_xpath(helpcenterMenuLocator))
          helpcenterElement.click()
          searchMenuElement = WebDriverWait(obj.driver,10).\
                              until(lambda driver:(obj.driver).find_element_by_xpath(searchMenuLocator))
          searchMenuElement.send_keys("fertile window")
          searchMenuElement.send_keys(Keys.RETURN)
          assert "no results found." not in (obj.driver).page_source
          time.sleep(6)
          obj.tearDown()
if __name__ == "__main__":       
      unittest.main()
