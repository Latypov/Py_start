from model.contacts import Contacts


def test_add_contact(app):
    app.contacts.create(Contacts(firstname="John", lastname="Smith", mob_phone="415 706 8792", email="john.smith@gmail.com"))


def test_add_empty_contact(app):
    app.contacts.create(Contacts(firstname="", lastname="", mob_phone="", email=""))

