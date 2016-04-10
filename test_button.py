from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
from testsetup import TestSetUp

class TestButton(unittest.TestCase):
      def test_waitForCheckOutGlowCommunity(self):
          obj = TestSetUp(webdriver.Chrome())        
          obj.setUp()
          bLocator = "/html/body/div[2]/section[3]/div/div/div[2]/a"
          seebutton = WebDriverWait(obj.driver, 10).until(EC.presence_of_element_located((By.XPATH, bLocator)))
          obj.tearDown()
if __name__ == "__main__":
       unittest.main()

