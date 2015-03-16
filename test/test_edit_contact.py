__author__ = 'allan'
from model.contacts import Contacts


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.edit_first_contact(Contacts(firstname="Samantha", lastname="Smith", mob_phone="415 706 8345", email="sam.smith@gmail.com"))
    app.session.logout()

