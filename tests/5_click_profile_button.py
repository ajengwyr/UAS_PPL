import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By

class ProfileTestCase(unittest.TestCase):

    @classmethod
    def setUp(self):
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
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
        self.browser.find_element(By.ID, 'inputUsername').send_keys('admin')
        self.browser.find_element(By.ID, 'inputPassword').send_keys('nimda666!')
        self.browser.find_element(By.TAG_NAME, 'button').click()

        # Verifikasi bahwa login berhasil
        expected_result = "Halo, admin"
        actual_result = self.browser.find_element(By.XPATH, "//h2[contains(text(),'Halo')]").text
        self.assertIn(expected_result, actual_result)

    def test_3_profile_click(self):
        expected_result = "Profil"
        self.browser.find_element(By.XPATH, "//a[contains(text(),'Profile')]").click()
        actual_result = self.browser.find_element(By.XPATH, "//h2[contains(text(),'Profile')]").text
        self.assertIn(expected_result, actual_result)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
