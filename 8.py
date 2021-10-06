import unittest
from selenium import webdriver

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

class TestSystem(unittest.TestCase):
    
    def test_last_name(self):
        lastname = browser.find_element_by_css_selector('.first_block>.second_class>.second')
        lastname.send_keys('Ivanov')
        self.assertEqual(lastname.get_attribute('placeholder'), 'Input your last name',
                         "last_name_past_error")
 


if __name__ == "__main__":
    unittest.main()
