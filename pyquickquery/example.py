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

query = Query(sqlite3.connect('test.db'), 'sqlite3')

# row = query.delete('users', where = {
#     'id': 15
# })


# print(row)


res = query.select(
            'users',
            ['id', 'login'],
            order_by = ['id', 'DESC']
        )()

print(res)



# a = query.create('users', {
#     'login' : 'killer51',
#     'password' : 'Password',
#     'token' : 'token'
# })
# print(a)

# a = query.update('users', {
#     'login' : 'killer51',
# }).where({"id" : 1})


# query.update('')