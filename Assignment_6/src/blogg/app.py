# -*- coding: utf-8 -*-
# imports
import sqlite3
from flask import Flask, request, g, redirect, url_for
from flask import abort, render_template, flash, jsonify

# configuration of global variables
DATABASE = 'blogg.db'
DEBUG = True
SECRET_KEY = 'test'

# create and initialize the app
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    """Collects data from the database."""
    db = get_db()
    cur = db.execute('select * from nyheter order by id desc')
    entries = cur.fetchall()
    return render_template('index.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    """Adds new data to the database."""
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


# ========================
# ====    Database    ====
# ========================

# connect to the database
def connect_db():
    """Connects to the database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


# create the database
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


# open connection to the database
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


# close connection to the database
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


# ------------------------------------
# Run application
if __name__ == '__main__':
    init_db()
    app.run()
