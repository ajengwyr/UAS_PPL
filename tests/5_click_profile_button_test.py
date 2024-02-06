import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By

class ProfileTestCase(unittest.TestCase):

    @classmethod
    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        self.browser = webdriver.Firefox(options=option)
        try:
            self.url = os.environ['URL']
        except:
            self.url = "http://localhost"
    
    def test(self):
        self.test_1_login_page()
        self.test_2_login_with_credentials()
        self.test_3_profile_click()

    def test_1_login_page(self):
        login_url = self.url +'/login.php'
        self.browser.get(login_url)
        
        expected_result = "Login"
        actual_result = self.browser.title
        self.assertIn(expected_result, actual_result)

    def test_2_login_with_credentials(self):
        # Masukkan username dan password
        self.browser.find_element(By.XPATH, "//*[@id='inputUsername']").send_keys('admin')
        self.browser.find_element(By.XPATH, "//*[@id='inputPassword']").send_keys('nimda666!')
        self.browser.find_element(By.XPATH, "/html/body/form/button").click()

        # Verifikasi bahwa login berhasil
        expected_result = "Halo, admin"
        actual_result = self.browser.find_element(By.XPATH, "/html/body/div[1]/h2").text
        self.assertIn(expected_result, actual_result)

    def test_3_profile_click(self):
        expected_result = "Profil"
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/a[1]").click()
        actual_result = self.browser.find_element(By.XPATH, "/html/body/div[1]/h2").text
        self.assertIn(expected_result, actual_result)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
