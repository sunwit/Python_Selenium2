from selenium import webdriver
import unittest
class TestSetUp(unittest.TestCase):                                                                                
      def __init__(self, dr):
          self.driver = dr 
      def setUp(self):  
          self.driver.get("http://www.glowing.com") 
      def tearDown(self):
          self.driver.quit()
if __name__ == "__main__":
      unittest.main()
             
