# GuessTheLanguage
Python Flask App for first QA Project, DevOps Core Fundementals.

## Introduction
This GitHub repository contains my source code for my first project.

## Contents

1. [Project Brief](#Project-Brief)
2. [Getting Started](#Getting-Started)
3. [Design](#Design)
4. [ERD](#ERD)
5. [Extended ERD](#extended-erd)
6. [CI Pipeline](#CI-Pipeline)
7. [Risk Assessment](#Risk-Assessment)
8. [Testing](#Testing)
9. [Known Issues](#Known-Issues)
10. [Future Work](#Future-Work)


## Project Brief

This project required me to design and produce a Flask web app of my choice as long as it has CRUD functionality (create, read, write & delete). The project was also based on the following topics:

* Project Management
* Python Fundamentals
* Python Testing
* Git
* Basic Linux
* Python Web Development
* Continuous Integration
* Cloud Fundamentals
* Databases

The web app is in Python using the Flask-framework and has a relational database. The database has 2 tables in a one-to-many relationship. 

The code had to be integrated via a Version Control System using the Feature Branch model then built via a CI server and deployed to a cloud-based virtual machine.

## Getting Started

Firstly I had to think of an idea to base my project on. I brainstormed using OneNote and came up with the GuessTheLanguage game idea. I then further developed this idea into a design.

## Design

I'm a keen language-learner so I decided to design a game where users can practice their ability to recognise languages. The web app includes a register / login system and the actual game itself under the "play" page. The user is required to register for an account in order to play the game. For simplicity I decided to only take an email address and a name.

Once a user is registered they're redirected to the login page and they'll be able to login using the details they registered with. The game itself allows the user to enter a sentence of their choice into the textbox and, using the Google Translate API - it translates that sentence into a random language. The user then has to guess what language they think it is and select it from the dropdown menu. When they click submit, the app will tell them if they got it right or wrong. If they got it right, the score count will increment. The highest winning streak gets stored in the database and the user will be able to see this under their profile.


## ERD

The relational database contains two tables "Users" and "Games". Below is the Entity Relationship Diagram.

![ERD diagram](https://github.com/AndreiChirovici1/GuessTheLanguage/blob/dev/ERD%20Guessthelang.drawio.png)


Future potential features:

- More stats on user's profile, for example join date, average playing time, best known languages

This is illustrated by the ERD diagram below: 

![Future ERD Diagram]()

## CI Pipeline

The key requirements of a CI pipeline are:

- Clear and tracked project requirements - usually using software specifically designed for this
- A version control system that maintains a single source code repository for the project
- Automated building of the application
- Automated testing with error reports generated
- Successful builds stored in an artefacts repository
- Automated deployment of the code

**Tracking**

I chose to use Trello for my task tracking.

My kanban board can be found [here.](https://trello.com/b/6bn5nwg2/devops-core-fundamentals-project)


**Version Control System**

I used git as my VCS and stored my source code in a repository on GitHub.

![Network Graph]()


**Automated Build and Testing**

Jenkins was used for the automation of the build and testing. 


## Risk Assessment


![Risk Assessment]()

## Testing

I conducted some unit testing using Pytest.


## Known Issues:



## Future Work:

