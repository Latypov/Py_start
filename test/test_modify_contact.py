__author__ = 'allan'
from model.contacts import Contacts


def test_modify_first_contact_name(app):
    old_contacts = app.contacts.get_contact_list()
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="Test"))
    app.contacts.modify_first_contact(Contacts(firstname="Samantha", lastname="Ford"))
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_first_contact_email(app):
    old_contacts = app.contacts.get_contact_list()
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="Test"))
    app.contacts.modify_first_contact(Contacts(email="Sam@gmail.com"))
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

