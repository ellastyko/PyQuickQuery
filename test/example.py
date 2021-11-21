#!/usr/bin/env python3
import sqlite3
import pymysql
from query import Query


# query = Query(pymysql.connect( 
#     host = 'localhost',
#     user = 'ella', 
#     password = 'password', 
#     db = 'name'
# ))

# query = Query(sqlite3.connect('test.db'))

# query.make('SELECT * FROM users;').all() # Make default query




u"hello"


# a = query.create('users', {
#     'login' : 'killer51',
#     'password' : 'Password',
#     'token' : 'token'
# })
# print(a)

# a = query.update('users', {
#     'login' : 'killer51',
# }).where({"id" : 1})

# row = query.select('users', ['login', 'password']).where({
#     'id': 1
# }).first()


# print(row)

# query.update('')