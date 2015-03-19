__author__ = 'allan'
from model.contacts import Contacts


def test_modify_first_contact_name(app):
    if app.contacts.count() > 0:
        app.contacts.modify_first_contact(Contacts(firstname="Samantha", lastname="Ford"))


def test_modify_first_contact_email(app):
    if app.contacts.count() > 0:
        app.contacts.modify_first_contact(Contacts(email="Sam@gmail.com"))

