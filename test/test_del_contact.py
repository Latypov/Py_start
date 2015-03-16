__author__ = 'allan'

import pytest
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.delete_first_contact()
    app.session.logout()
