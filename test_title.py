from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
from testsetup import TestSetUp

class AssertTitle(unittest.TestCase):
      def test_title(self):
          obj = TestSetUp(webdriver.Chrome())
          obj.setUp()
          self.assertEqual(obj.driver.title, "Glow - Health Demystified by Data")
          obj.tearDown()
if __name__ == "__main__":
       unittest.main()
