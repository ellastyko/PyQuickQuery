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


a = query.create('users', {
    'login' : 'new_user',
    'password' : 'Password',
    'token' : 'token'
})
print(a)


res = query.select(
            'users',
        )()

print(res)

a = query.update('users', {
    "login": 'omagadble'
}, {
    'id' : 0
})
print(a)


res = query.select(
            'users',
            where={'id' : 17}
        )()

print(res)



query.delete('users', {
    'id': 2
})

res = query.select(
            'users'
        )(3)

print(res)
