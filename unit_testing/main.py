import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class capstone(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\my pc\\Desktop\\chromedriver.exe")

    def test_url(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.assertTrue(self.driver.find_element_by_link_text('Sign in'))

    def test_explore_button(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element_by_css_selector('#content > div:nth-child(2) > div > div:nth-child(2) > div.col > a').click()
        self.assertTrue(self.driver.find_element_by_link_text('iPhone'))



        
    def test_login_correct(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element_by_link_text('Sign in').click()
        self.driver.find_element_by_name('username').send_keys('Kamal')
        self.driver.find_element_by_name('password').send_keys('kamal12$')
        self.driver.find_element_by_css_selector('#content > div > div > div > form > p > input[type=submit]').click()
        self.assertTrue(self.driver.find_element_by_link_text('iPhone'))

    # def test_login_uncorrect(self):
    #     self.driver.get("http://127.0.0.1:8000/")
    #     self.driver.find_element_by_link_text('Sign in').click()
    #     self.driver.find_element_by_name('username').send_keys('Kamal')
    #     self.driver.find_element_by_name('password').send_keys('kkamal12$')
    #     self.driver.find_element_by_css_selector('#content > div > div > div > form > p > input[type=submit]').click()
    #     self.assertTrue(self.driver.find_elements_by_class_name('athena-shortcut-div'))

    def test_product(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element_by_link_text('Sign in').click()
        self.driver.find_element_by_name('username').send_keys('Kamal')
        self.driver.find_element_by_name('password').send_keys('kamal12$')
        self.driver.find_element_by_css_selector('#content > div > div > div > form > p > input[type=submit]').click()
        self.driver.find_element_by_link_text('iPhone').click()
        self.assertTrue(self.driver.find_element_by_css_selector('#concard > div > p:nth-child(4) > button'))


    def test_negotiate_button(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element_by_link_text('Sign in').click()
        self.driver.find_element_by_name('username').send_keys('Kamal')
        self.driver.find_element_by_name('password').send_keys('kamal12$')
        self.driver.find_element_by_css_selector('#content > div > div > div > form > p > input[type=submit]').click()
        self.driver.find_element_by_link_text('iPhone').click()
        self.driver.find_element_by_css_selector('#concard > div > p:nth-child(4) > button').click()
        self.assertTrue(self.driver.find_element_by_css_selector('#myForm > div > div > form > input[type=text]:nth-child(1)'))





    def tearDown(self):
        self.driver.close()
        



if __name__ == "__main__":
    unittest.main()
    

    
     













    