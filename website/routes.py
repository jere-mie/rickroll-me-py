from flask import render_template, url_for, flash, redirect, request
from website import app, db, login_manager
from website.forms import LinkForm, EditForm, LoginForm
from website.models import Link, User
import json
import re
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

@login_manager.user_loader
def user_loader(username):
  user = User()
  user.id = username
  return user

@app.route('/home', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    with open('config.json') as f:
        data = json.load(f)
    if form.validate_on_submit():
        if form.password.data == data['password']:
            user = User()
            user.id = "Rick"
            login_user(user, remember=True)
            flash('login worked', 'success')
            return redirect(url_for('home'))
        else:
            flash('incorrect password!', 'danger')
    return render_template('login.html', form=form, data=data)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/admin', methods=['GET'])
@login_required
def admin():
    links = Link.query.all()
    with open('config.json') as f:
        data = json.load(f)
    return render_template('admin.html', links=links, domain=data['domain'])

@app.route('/new', methods=['GET', 'POST'])
def new():
    form = LinkForm()
    if form.validate_on_submit():
        link = Link(link=form.link.data, title=form.title.data, name = form.name.data, desc=form.desc.data, image=form.image.data, url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        link.link = link.link.replace(' ','-')
        link.link = re.sub(r'[^a-zA-Z0-9-]', '-', link.link)
        db.session.add(link)
        db.session.commit()
        # getting config details
        with open('config.json') as f:
            data = json.load(f)
        flash(f"Created link {data['domain']}/l/{link.link}", 'success')
        return redirect(url_for('home'))
    return render_template('new.html', form=form, legend='New Link')

@app.route('/l/<link_url>/edit', methods=['GET', 'POST'])
@login_required
def edit(link_url):
    link = Link.query.filter_by(link=link_url).first()
    form = EditForm()
    if form.validate_on_submit():
        link.link = form.link.data
        link.url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        link.title = form.title.data
        link.name = form.name.data
        link.desc = form.desc.data
        link.image = form.image.data
        
        db.session.commit()
        flash('Successfully updated link!', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.link.data = link.link
        # form.url.data = link.url
        form.title.data = link.title
        form.name.data = link.name
        form.desc.data = link.desc
        form.image.data = link.image
                
    return render_template('new.html', form=form, legend='Update Link')

@app.route('/l/<link_url>', methods=['GET'])
def redir(link_url):
    link = Link.query.filter_by(link=link_url).first()
    return render_template('redir.html', title=link.title, name=link.name, desc=link.desc, image=link.image, url=link.url)

@app.route('/l/<link_url>/delete', methods=['GET','POST'])
@login_required
def delete(link_url):
    link = Link.query.filter_by(link=link_url).first()
    db.session.delete(link)
    db.session.commit()
    flash('Successfully deleted link!', 'success')
    return redirect(url_for('home'))