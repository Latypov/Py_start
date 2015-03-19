__author__ = 'allan'
from model.contacts import Contacts

def test_delete_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="Test"))
    app.contacts.delete_first_contact()

