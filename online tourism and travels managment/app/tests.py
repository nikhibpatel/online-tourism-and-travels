from django.test import TestCase
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

# Create your tests here.

class TestProjectListPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser=webdriver.Chrome('chromedriver.exe')

    def tearDown(self): 
        self.browser.close()

    def Test(self):
        self.browser.get('http://127.0.0.1:8000/app/login/')
        self.browser.maximize_window() 
        self.browser.find_element_by_name("username").send_keys("nikhil")
        time.sleep(1)
        self.browser.find_element_by_name("password").send_keys("nikhil")
        time.sleep(1)
        self.browser.find_element_by_class_name("btn").click()
        time.sleep(5)

        self.browser.find_element_by_class_name("bus").click()

        self.browser.find_element_by_name("source").send_keys("nadiad")
        time.sleep(1)
        self.browser.find_element_by_name("destination").send_keys("rajkot")
        time.sleep(3)
        self.browser.find_element_by_class_name("btn").click()
        time.sleep(3)
        link = self.browser.find_element_by_link_text('Reserve')
        link.click()

        time.sleep(2)
        self.browser.find_element_by_name("name").send_keys("nikhil")
        time.sleep(1)
        self.browser.find_element_by_name("age").send_keys("2")
        time.sleep(1)
        self.browser.find_element_by_name("phone").send_keys("1212121212")
        time.sleep(1)
        self.browser.find_element_by_name("email").send_keys("nnn@gmail.com")
        time.sleep(1)
        self.browser.find_element_by_name("seat").send_keys("1")
        time.sleep(5)
        self.browser.find_element_by_class_name("btn").click()

        self.browser.find_element_by_name("card_num").send_keys("451212121245")
        time.sleep(1)
        self.browser.find_element_by_name("month").send_keys("january")
        time.sleep(1)
        self.browser.find_element_by_name("year").send_keys("2023")
        time.sleep(1)
        self.browser.find_element_by_name("cvv").send_keys("123")
        time.sleep(5)

        self.browser.find_element_by_name("submit").click()
        time.sleep(3)

        self.browser.find_element_by_link_text("Home").click()
        time.sleep(3)

        self.browser.find_element_by_link_text("My Bookings").click()
        time.sleep(3)

        self.browser.find_element_by_link_text("Cancel").click()
        time.sleep(3)
