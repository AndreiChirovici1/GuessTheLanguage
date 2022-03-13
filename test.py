from flask import Flask, redirect, render_template, url_for
from flask_testing import TestCase
from app import app
import unittest
import pytest

# Unit Testing

# Unit Testing Configuration

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app.config['TESTING'] = True
        self.app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass
    
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_contact_get(self):
        response = self.client.get(url_for('contact'))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()