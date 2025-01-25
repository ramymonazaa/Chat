A basic chat site built with Django that provides real-time communication and user interaction. 
This project serves as a foundation for a chat platform and is currently under development, with plans to add new features in the future.
Features:

Authentication
  - Sign Up: Create a new account.
  - Log In: Log in with your registered username.
  - Log Out: Securely log out of your account.

User List
  - View a list of all users on the site.
  - Connect with any user directly via a button below their name.

Chat Rooms (Groups)
  - View a list of rooms (groups) you are a member of.
  - Create new rooms to communicate with multiple users.


Installation

Prerequisites
  - Python 3.9+
  - Django 4.0+

Steps to Set Up
  - git clone (https://github.com/ramymonazaa/Chat.git)
  - cd chat-website
  - python -m venv venv
  - source venv/bin/activate  # On Windows: venv\Scripts\activate
  - python manage.py migrate
  - python manage.py runserver
