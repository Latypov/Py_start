from model.contacts import Contacts


def test_add_contact(app):
    old_contacts = app.contacts.get_contact_list()
    contact = Contacts(firstname="John", lastname="Smith", mob_phone="415 706 8792", email="john.smith@gmail.com")
    app.contacts.create(contact)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contacts.get_contact_list()
    app.contacts.create(Contacts(firstname="", lastname="", mob_phone="", email=""))
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

