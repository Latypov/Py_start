from model.contacts import Contacts


def test_add_contact(app):
    old_contacts = app.contacts.get_contact_list()
    app.contacts.create(Contacts(firstname="John", lastname="Smith", mob_phone="415 706 8792", email="john.smith@gmail.com"))
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contacts.get_contact_list()
    app.contacts.create(Contacts(firstname="", lastname="", mob_phone="", email=""))
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

