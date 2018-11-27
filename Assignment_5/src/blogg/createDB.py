#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
conn = sqlite3.connect('blogg.db')
print('Opened database successfully')

conn.execute('''drop table if exists nyheter;''')

conn.execute('''create table nyheter (
    id integer primary key autoincrement, 
    tittel text not null, 
    nyhet text not null, 
    forfatter text not null,
    dato text not null);''')
print('Table created successfully')

conn.close()
