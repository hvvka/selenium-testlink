import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrg(unittest.TestCase):
    grail_results = ""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_documentation(self):
        driver = self.driver
        driver.get("https://www.python.org/")
        self.assertEqual("Welcome to Python.org", driver.title)
        driver.find_element_by_link_text("Docs").click()
        self.assertEqual("Python 3.6.5 documentation", driver.find_element_by_xpath("//h1").text)
        driver.find_element_by_name("q").click()
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys("selenium")
        driver.find_element_by_name("q").send_keys(Keys.ENTER)
        result = driver.find_element_by_xpath("//div[@id='search-results']/p").text
        self.assertEqual(result,
                         driver.find_element_by_xpath("//div[@id='search-results']/p").text)

    def test_events(self):
        driver = self.driver
        driver.get("https://www.python.org/")
        driver.find_element_by_link_text("Events").click()
        self.assertEqual("Upcoming Events",
                         driver.find_element_by_xpath("//div[@id='content']/div/section/div/div/h2").text)
        driver.find_element_by_xpath("//div[@id='content']/div/section/div/div/ul/li/p/time").click()
        date = driver.find_element_by_xpath("//div[@id='content']/div/section/div/div/ul/li/p/time").text
        self.assertEqual(date,
                         driver.find_element_by_xpath("//div[@id='content']/div/section/div/div/ul/li/p/time").text)

    def test_list(self):
        global grail_results
        driver = self.driver
        driver.get("https://www.python.org/")
        driver.find_element_by_id("id-search-field").click()
        driver.find_element_by_id("id-search-field").clear()
        driver.find_element_by_id("id-search-field").send_keys("grail")
        driver.find_element_by_id("id-search-field").send_keys(Keys.ENTER)
        self.assertEqual("Glue It All Together With Python",
                         driver.find_element_by_link_text("Glue It All Together With Python").text)
        grail_results = driver.find_element_by_xpath("//div[@id='content']/div/section/form/ul/li[6]/p").text

    def test_list_again(self):
        driver = self.driver
        driver.get("https://www.python.org/")
        driver.find_element_by_id("id-search-field").click()
        driver.find_element_by_id("id-search-field").clear()
        driver.find_element_by_id("id-search-field").send_keys("grail")
        driver.find_element_by_id("id-search-field").send_keys(Keys.ENTER)
        self.assertEqual("Glue It All Together With Python",
                         driver.find_element_by_link_text("Glue It All Together With Python").text)
        results = driver.find_element_by_xpath("//div[@id='content']/div/section/form/ul/li[6]/p").text
        self.assertEqual(grail_results, results)

    def test_search(self):
        driver = self.driver
        driver.get("https://www.python.org/")
        driver.find_element_by_id("id-search-field").click()
        driver.find_element_by_id("id-search-field").clear()
        driver.find_element_by_id("id-search-field").send_keys("monty")
        driver.find_element_by_id("submit").click()
        self.assertEqual("Welcome to Python.org", driver.title)
        try:
            self.assertEqual("Foreword for \"Programming Python\" (1st ed.)",
                             driver.find_element_by_link_text("Foreword for \"Programming Python\" (1st ed.)").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual("Python For Beginners", driver.find_element_by_link_text("Python For Beginners").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual("[PYTHON MATRIX-SIG] FAQ",
                             driver.find_element_by_link_text("[PYTHON MATRIX-SIG] FAQ").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
