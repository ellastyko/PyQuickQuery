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

query = Query(sqlite3.connect('test.db'))

# query.make('SELECT * FROM users;').all() # Make default query







# a = query.create('users', {
#     'name' : 'Sarah',
#     'login' : 'killer51',
#     'token' : 'token'
# })

row = query.select('users', ['login', 'password']).where({
    'id': 1
}).first()


print(row)

# query.update('')