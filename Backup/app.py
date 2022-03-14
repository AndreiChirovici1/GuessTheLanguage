from flask import Flask, redirect, render_template, url_for, request, Response, session, flash
from flask_testing import TestCase
from flask_mail import Mail, Message
from random import randrange
import os
from google.cloud import translate_v2 as translate
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/Users/craig/Documents/Andrei-Project/Chatalot 2.0/GoogleCloudKey.json"
import six
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import session as sql_session
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

app = Flask(__name__)
app.secret_key = 'averysecretkey1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 


# Database
db = SQLAlchemy(app)

class users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))  
    game = db.relationship('games', backref='users')

class games(db.Model):
    gameid = db.Column(db.Integer, primary_key = True)
    scoreStreak = db.Column(db.Integer)
    fk_user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)

def __init__(self, name, email, scoreStreak, fk_user_id):
    self.name = name
    self.email = email
    self.scoreStreak = scoreStreak
    self.fk_user_id = fk_user_id