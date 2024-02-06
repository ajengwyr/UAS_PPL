from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class CorrectLoginTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.browser = webdriver.Firefox()
#        self.addCleanup(self.browser.quit)
    
    def test_1_login_page(self):
        self.browser.get('http://localhost/BadCRUD/login.php')
        expected_result = "Login"        
        actual_result = self.browser.title
        self.assertIn(expected_result, actual_result)
    
    def test_2_login_click(self):           
        expected_result = "Wrong usename or password"
        self.browser.find_element(By.XPATH, "//*[@id='inputUsername']").send_keys("admin")
        self.browser.find_element(By.XPATH, "//*[@id='inputPassword']").send_keys("halo")
        self.browser.find_element(By.XPATH, "/html/body/form/button").click()
        actual_result = self.browser.find_element(By.XPATH, "/html/body/form/div/label").text                
        self.assertIn(expected_result, actual_result)
    
    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')