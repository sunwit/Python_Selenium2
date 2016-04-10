from selenium import webdriver
import unittest
class testWindow(unittest.TestCase):
      def testWindowVisit(self):
          global driver
          driver = webdriver.Chrome()
          first_url = 'http://www.glowing.com'
          print("now access %s" %(first_url))
          driver.get(first_url)
          second_url = 'http://www.glowing.com/community'
          print("now access %s" %(second_url))
          driver.get(second_url)
          print("back to %s" %(first_url))
          driver.back()
          print("forward to %s" %(second_url))
          driver.forward()
      def tearDown(self):
          driver.quit()
if __name__ == "__main__":
      unittest.main()
          
          
