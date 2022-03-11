from flask import Flask, redirect, render_template, url_for, request, Response, session, flash
from flask_mail import Mail, Message
from random import randrange
import os
from google.cloud import translate_v2 as translate
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/Users/craig/Documents/Andrei-Project/Chatalot 2.0/GoogleCloudKey.json"
import six
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.secret_key = 'averysecretkey1'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'

# Database
db = SQLAlchemy(app)

class users(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))  

class games(db.Model):
    __tablename__ = "games"
    gameid = db.Column('game_id', db.Integer, primary_key = True)
    fk_user_id = db.Column(Integer, ForeignKey('users.user_id'))
    scoreStreak = db.Column(db.Integer)  

def __init__(self, name, email):
    self.name = name
    self.email = email

def __init__(self, scoreStreak):
    self.scoreStreak = scoreStreak

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/play', methods=['GET', 'POST'])
def play():
    if 'email' not in session:
        return redirect(url_for('register'))
    if request.method == 'POST':
        # Input text from form
        text = request.form['inputtext']
        streakscore = request.form['scorelabel']
        userselection = request.form.get('langs')
        
        # Array storing codes of Google Analytics' supported languages 
        langs = ["af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "zh", "zh-TW", "co", "hr", "cs", "da", "nl", "en", "eo", "et", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", "he", "hi", "hmn", "hu", "is", "ig", "id", "ga", "it", "ja", "jv", "kn", "kk", "km", "rw", "ko", "ku", "ky", "lo", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "ny", "or", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tl", "tg", "ta", "tt", "te", "th", "tr", "tk", "uk", "ur", "ug", "uz", "vi", "cy", "xh", "yi", "yo", "zu"]
        # Length of Array - 108
        noLangs = len(langs)
        # Random number generator between 0 and 107
        randomNumber = randrange(noLangs)

        # Initialising translation
        client = translate.Client()
        
        # Target language is random
        target = langs[randomNumber]

        # Output from Google Translate's API
        output = client.translate(
            text,
            target_language=target
        )
        useremail = session['email']
        if target == userselection:
            # Streak score should update from JS on page
            # Query to get userID by email logged into session
            user = users.query.filter_by(email=useremail).first()
            userid = user.id
            if games.query.filter_by(fk_user_id=userid).first() is None:
                game = games(fk_user_id = userid, scoreStreak = streakscore)
                db.session.add(game)
                db.session.commit()
            else:
                session.query(games).update({games.scoreStreak == streakscore})
                db.session.commit()

        translatedText = output['translatedText']
        # Adding values to session so that we can display on page
        session['input'] = text
        session['output'] = translatedText
        session["target"] = target
        user = users.query.filter_by(email=useremail).first()
        userid = user.id
        latestgame = games.query.filter_by(fk_user_id = userid).first()
        latestscore = latestgame.scoreStreak
        session['latestscore'] = latestscore
        print(translatedText)
        print(output)
        print(target)
    return render_template('play.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/instructions')
def instructions():
    return render_template('instructions.html')

@app.route('/languages')
def languages():
    return render_template('languages.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'email' in session:
        return redirect(url_for('home'))

    if request.method == "POST":
        name = request.form['firstname']
        emailform = request.form['emailinput']

        user = users.query.filter_by(email=emailform).first()
        emaildb = user.email
        print(emaildb)

        if emaildb == emailform:
            # Adding user to session
            session['email'] = emailform
            return redirect(url_for('play'))
        else:
            flash('Name or email entered incorrect', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'email' in session:
        return redirect(url_for('home'))

    if request.method == "POST":
        
        # Data validation
        if not request.form['firstname'] or not request.form['emailinput']:
            flash('Please enter all required details', 'error')
        else:
            user = users(name = request.form['firstname'], email = request.form['emailinput'])
            game = games(fk_user_id = user.id, scoreStreak = 0)
            # Take user details and store in DB

            db.session.add(user)
            db.session.commit()
        
            # Emailing user
            #app.config['MAIL_SERVER'] = 'smtp.gmail.com'
            #app.config['MAIL_PORT'] = 465
            #app.config['MAIL_PASSWORD'] = ''
            #app.config['MAIL_USERNAME'] = 'andrei.chirovici@gmail.com'
            #app.config['MAIL_USE_TLS'] = False
            #app.config['MAIL_USE_SSL'] = True
            #mail = Mail(app)
            #msg = Message("Guess The Language Registration", sender="andrei.chirovici@gmail.com", recipients=[request.form['emailinput']])
            #msg.body = "Hello, welcome to guess the language! Enjoy playing!"
            #mail.send(msg)
            
            flash('Record was successfully added')
            return redirect(url_for('login'))

    return render_template('register.html')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)