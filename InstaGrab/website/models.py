from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    cookies = db.Column(db.String(5000))

class UsernameList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listname = db.Column(db.String(100))
    list = db.Column(db.String(50000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))