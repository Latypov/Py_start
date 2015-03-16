import pytest
from model.contacts import Contacts
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.fill_contact_form(Contacts(firstname="John", lastname="Smith", mob_phone="415 706 8792", email="john.smith@gmail.com"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.fill_contact_form(Contacts(firstname="", lastname="", mob_phone="", email=""))
    app.session.logout()

