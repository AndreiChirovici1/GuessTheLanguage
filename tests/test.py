from flask import url_for
from flask_testing import TestCase
import pytest
from app import db, users, games, app
import app

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///users.sqlite3',
            SECRET_KEY = 'mysecretkey',
            DEBUG_MODE = True,
            WTF_CSRF_ENABLED = False
        )
        return app

    def setUp(self):
        db.create_all()
        test_user = users(name="Andrei", email="andrei.chirovici@gmail.com")
        db.session.add(test_user)
        db.session.commit()

def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestHome(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)

class TestAddUser(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('register'))
        self.assert200(response)
    
    def test_create_post(self):
        response = self.client.post(
            url_for('register'),
            data = dict(name="Andrei", email="andrei.chirovici@gmail.com"),
            follow_redirects = True
        )
        self.assert200(response)