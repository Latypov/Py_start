# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contacts import Contacts

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def add_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()

    def fill_contact_form(self, wd, contacts):
        self.add_new_contact(wd)
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contacts.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contacts.lastname)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contacts.mob_phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contacts.email)
        wd.find_element_by_name("submit").click()
        self.return_to_home_page(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def test_test_add_contact(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.fill_contact_form(wd, Contacts(firstname="John", lastname="Smith", mob_phone="415 706 8792", email="john.smith@gmail.com"))
        self.logout(wd)

    def test_test_add_empty_contact(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.fill_contact_form(wd, Contacts(firstname="", lastname="", mob_phone="", email=""))
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
