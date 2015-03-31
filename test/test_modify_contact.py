__author__ = 'allan'
from model.contacts import Contacts


def test_modify_first_contact_name(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="Test"))
    old_contacts = app.contacts.get_contact_list()
    contact = Contacts(firstname="Samantha", lastname="Ford")
    contact.id = old_contacts[0].id
    app.contacts.modify_first_contact(contact)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)


#def test_modify_first_contact_email(app):
#    old_contacts = app.contacts.get_contact_list()
#    if app.contacts.count() == 0:
#        app.contacts.create(Contacts(firstname="Test"))
#    app.contacts.modify_first_contact(Contacts(email="Sam@gmail.com"))
#    new_contacts = app.contacts.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)

