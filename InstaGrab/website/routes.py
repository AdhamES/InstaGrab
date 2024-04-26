from flask import Blueprint, render_template, redirect, request, url_for, flash, session

import json

from .models import User, UsernameList
from . import db
from .automation import Auto


routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('home.html', active_page='home')

@routes.route('/toolhub')
def toolHub():
    if 'user' in session:
        currentUser = User.query.filter_by(username=session['user']).first()
        usernameLists = UsernameList.query.filter_by(user_id=currentUser.id).all()
        data = []
        for uList in usernameLists:
            data.append({'id': uList.id, 'name':uList.listname, 'usernames': json.loads(uList.list)})
        return render_template('toolhub.html', active_page='toolhub', data=data)
    else:
        flash('You need to login to access this page.', category='error')
        return redirect(url_for('routes.login'))
    
@routes.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        flash('You are already logged in !', category='error')
        return redirect(url_for('routes.toolHub'))
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        auto = Auto()
        if user:
            auto.loadCookies(json.loads(user.cookies))
            auto.refresh()
            if auto.isLogged():
                flash('Logged in successfully, welcome back !', category='success')
                session['user'] = username
                auto.quit()
                return redirect(url_for('routes.toolHub'))
            else:
                auto.login(username, password)
                cookies = auto.getCookies()
                user.cookies = json.dumps(cookies)
                session['user'] = username
                flash('Logged in successfully, welcome back !', category='success')
                auto.quit()
                return redirect(url_for('routes.toolHub'))
        else:
            auto.login(username, password)
            if auto.isLogged():
                cookies = auto.getCookies()
                new_user = User(username=username, password = password, cookies = json.dumps(cookies))
                db.session.add(new_user)
                db.session.commit()
                session['user'] = username
                flash('Logged in successfully!', category='success')
                auto.quit()
                return redirect(url_for('routes.toolHub'))
            else:
                flash('Username or e-mail is incorrect, try again', category='error')
                auto.quit()
                return render_template('login.html')
    else:
        return render_template('login.html', active_page='login')

@routes.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        flash('Logged out successfully !', category='success')
        return redirect(url_for('routes.home'))
    else:
        flash('You are already logged out', category='error')
        return redirect(url_for('routes.home'))
    
@routes.route('/newlist', methods=['POST'])
def newList():
    listName = request.form['listname']
    currentUser = User.query.filter_by(username=session['user']).first()
    newlist = UsernameList(user_id=currentUser.id, listname=listName, list=json.dumps([]))
    db.session.add(newlist)
    db.session.commit()
    return redirect(url_for('routes.toolHub'))

@routes.route('/deletelist', methods=['POST'])
def deleteList():
    listId = request.form['listId']
    currentUser = User.query.filter_by(username=session['user']).first()
    UsernameList.query.filter_by(id=listId, user_id=currentUser.id).delete()
    db.session.commit()
    return redirect(url_for('routes.toolHub'))

@routes.route('/addusernames', methods=['POST'])
def addUsernames():
    listId = int(request.form['listId'])
    fromAccount = request.form['fromaccount']

    # currentUser = User.query.filter_by(username=session['user']).first()
    listToUpdate = UsernameList.query.filter_by(id=listId).first()
    listContent = json.loads(listToUpdate.list)
    newListContent = listContent
    
    auto = Auto()

    usernames = auto.getUsernames(fromAccount)

    for usr in usernames:
        if usr not in listContent:
            newListContent.append(usr)

    listToUpdate.list = json.dumps(newListContent)
    
    db.session.commit()

    return redirect(url_for('routes.toolHub'))

@routes.route('/sendmessage', methods = ['POST'])
def sendMessage():
    message = request.form['message']
    listId = request.form['listId']
    currentUser = User.query.filter_by(username=session['user']).first()
    userList = UsernameList.query.filter_by(id=listId).first()
    listContent = json.loads(userList.list)

    auto = Auto()
    auto.loadCookies(json.loads(currentUser.cookies))

    auto.sendMessage(message, listContent)
    
    return redirect(url_for('routes.toolhub'))