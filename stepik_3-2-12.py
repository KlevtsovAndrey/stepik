import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./drivers/chromedriver.exe')

    def test_abs1(self):
        driver = self.driver
        link = "http://suninjuly.github.io/registration1.html"
        driver.get(link)
        driver.implicitly_wait(5)
        fisrtname = driver.find_element(By.XPATH, '//div[@class="first_block"]/div/input[@class="form-control first"]')
        lastname = driver.find_element(By.XPATH, '//div[@class="first_block"]/div/input[@class="form-control second"]')
        email = driver.find_element(By.XPATH, '//div[@class="first_block"]/div/input[@class="form-control third"]')
        fisrtname.send_keys('firstname')
        lastname.send_keys('lastname')
        email.send_keys('email')
        button = driver.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(3)
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text

    def test_abs2(self):
        driver = self.driver
        link = "http://suninjuly.github.io/registration2.html"
        driver.get(link)
        driver.implicitly_wait(5)
        fisrtname = driver.find_element(By.XPATH, '//div[@class="first_block"]/div/input[@class="form-control first"]')
        lastname = driver.find_element(By.XPATH, '//div[@class="first_block"]/div/input[@class="form-control second"]')
        email = driver.find_element(By.XPATH, '//div[@class="first_block"]/div/input[@class="form-control third"]')
        fisrtname.send_keys('firstname')
        lastname.send_keys('lastname')
        email.send_keys('email')
        button = driver.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
