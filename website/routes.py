from flask import render_template, url_for, flash, redirect, request
from website import app, db
from website.forms import LinkForm
from website.models import Link

# from flask_login import login_user, current_user, logout_user, login_required

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     form = Login()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user and form.password.data==user.password:
#             login_user(user, remember=form.remember.data)
#             return redirect(url_for('home'))
#         else:
#             flash('Error Logging In', 'danger')
#     return render_template("login.html", form=form)

# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('home'))

@app.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    form = Link()
    if form.validate_on_submit():
        link = Link(link=form.link.data, title=form.title.data, name = form.name.data, desc=form.desc.data, image=form.image.data)
        db.session.add(link)
        db.session.commit()
        flash(f'Created link exampledomain.tld/{form.link.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('new.html', form=form, legend='New Link')

@app.route('/<link_url>/edit', methods=['GET', 'POST'])
@login_required
def edit(link_url):
    link = Link.query.get_or_404(link_url)
    form = LinkForm()
    if form.validate_on_submit():
        link.link = form.link.data
        link.title = form.title.data
        link.name = form.name.data
        link.desc = form.desc.data
        link.image = form.image.data
        
        db.session.commit()
        flash('Successfully updated link!', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.link.data = link.link
        form.title.data = link.title
        form.name.data = link.name
        form.desc.data = link.desc
        form.image.data = link.image
                
    return render_template('new.html', form=form, legend='Update Link')

@app.route('/l/<link_url>', methods=['GET'])
def redir(link_url):
    link = Link.query.get_or_404(link_url)
    return render_template('redir.html', name=link.name, title=link.title, desc=link.desc, image=link.image, url=link.link)