__author__ = 'allan'
from model.contacts import Contacts
from random import randrange


def test_modify_contact_name(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(lastname="Test"))
    old_contacts = app.contacts.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contacts(firstname = "Sam", lastname="Ford")
    contact.id = old_contacts[index].id
    app.contacts.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)


#def test_modify_first_contact_email(app):
#    old_contacts = app.contacts.get_contact_list()
#    if app.contacts.count() == 0:
#        app.contacts.create(Contacts(firstname="Test"))
#    app.contacts.modify_first_contact(Contacts(email="Sam@gmail.com"))
#    new_contacts = app.contacts.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)

