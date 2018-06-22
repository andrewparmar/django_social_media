from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
	
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):    
        self.browser.quit()
        
    def test_can_login(self):    
        # User logs onto online bookmark app
        self.browser.get('http://localhost:8000/account')
        
        # page title is Quant
        self.assertIn('Quant', self.browser.title)
        self.fail('Finish the test')

        # user click on login page to login


if __name__ == '__main__':
    unittest.main(warnings='ignore')
