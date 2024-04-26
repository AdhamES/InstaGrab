from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = 'juguyjtjhg'
    db.init_app(app)

    from .models import User, UsernameList
    with app.app_context():
        db.create_all()
        ### a supprimer
        '''import json
        dummyUser = User(username='foobar', email='foobar@gmail.com', password='fooBar_1234')
        dummyList1 = UsernameList(user_id=1, listname='list1', list=json.dumps(['user1', 'user2', 'user3']))
        dummyList2 = UsernameList(user_id=1, listname='list2', list=json.dumps(['insta_user', 'another_user']))
        dummyList3 = UsernameList(user_id=1, listname='list3', list=json.dumps(['cool_insta', 'awesome_user', 'insta_lover']))
        dummyList4 = UsernameList(user_id=1, listname='list4', list=json.dumps(['fashion_insta', 'style_guru']))
        dummyList5 = UsernameList(user_id=1, listname='list5', list=json.dumps(['foodie_insta', 'yummy_user', 'chef_master']))
        db.session.add(dummyUser)
        db.session.add(dummyList1)
        db.session.add(dummyList2)
        db.session.add(dummyList3)
        db.session.add(dummyList4)
        db.session.add(dummyList5)
        db.session.commit()'''
        ###

    from .routes import routes

    app.register_blueprint(routes, url_prefix='/')

    return app