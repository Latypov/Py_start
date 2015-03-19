from model import contacts

__author__ = 'allan'
from model.contacts import Contacts
import fixture.application


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contacts):
        wd = self.app.wd
        self.add_new_contact()
        self.fill_contact_form(contacts)
        #submit new contact
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_first_contact()
        #delete selection
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contacts):
        wd = self.app.wd
        self.type("firstname", contacts.firstname)
        self.type("lastname", contacts.lastname)
        self.type("mobile", contacts.mobile)
        self.type("email", contacts.email)

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_first_contact()
        #open modification form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        #update contact
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))
