# -*- coding: utf-8 -*-
# imports
import sqlite3
import os
from flask import Flask, request, g, session, redirect, url_for
from flask import abort, render_template, flash, jsonify
from forms.loginform import LoginForm

# configuration of global variables
DATABASE = 'blogg.db'
DEBUG = True
SECRET_KEY = 'test'

# create and initialize the app
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.urandom(32)


# INDEX + SESSION
@app.route('/')
def index():
    """Collects data from the database."""
    db = get_db()
    cur = db.execute('select * from nyheter order by id desc')
    entries = cur.fetchall()

    if 'username' in session:
        return render_template('index.html', entries=entries, loggedin=True)
    return render_template('index.html', entries=entries, loggedin=False)


# ================= #

# ====  LOGIN  ==== #
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('index'))
    return render_template("login.html", form=form)


@app.route('/add', methods=['POST'])
def add_entry():
    """Posts data to the database."""
    db = get_db()
    db.execute('insert into nyheter (tittel, nyhet, forfatter, dato) '
               'values(?, ?, ?, datetime(\'now\', \'localtime\'))',
        [request.form['tittel'],
         request.form['nyhet'],
         request.form['forfatter']]
    )
    db.commit()
    flash('Innlegget ble sendt og lagret i databasen')
    return redirect(url_for('index'))


@app.route('/delete/<post_id>', methods=['GET'])
def delete_entry(post_id):
    """Delete post from database."""
    result = {'status': 0, 'message': 'Error'}
    try:
        db = get_db()
        db.execute('delete from nyheter where id=' + post_id)
        db.commit()
        result = {'status': 1, 'message': 'Post Deleted'}
    except Exception as e:
        result = {'status': 0, 'message': repr(e)}
    return jsonify(result)


# ======================== #
# ====    Database    ==== #
# ======================== #

# CONNECT to the database
def connect_db():
    """Connects to the database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


# CREATE the database
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


# OPEN connection to the database
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


# CLOSE connection to the database
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


# ---------------------
# -- Run application --
if __name__ == '__main__':
    init_db()
    app.run(port=8080)
