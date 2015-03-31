__author__ = 'allan'
from model.contacts import Contacts

def test_delete_first_contact(app):
    old_contacts = app.contacts.get_contact_list()
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="Test"))
    app.contacts.delete_first_contact()
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
