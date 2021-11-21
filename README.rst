.. image:: https://readthedocs.org/projects/pymysql/badge/?version=latest
    :target: https://pymysql.readthedocs.io/
    :alt: Documentation Status

.. image:: https://coveralls.io/repos/PyMySQL/PyMySQL/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/PyMySQL/PyMySQL?branch=master

.. image:: https://img.shields.io/lgtm/grade/python/g/PyMySQL/PyMySQL.svg?logo=lgtm&logoWidth=18
    :target: https://lgtm.com/projects/g/PyMySQL/PyMySQL/context:python


PyQuickQuery
=======

.. contents:: Table of Contents
   :local:


Requirements
-------------

* Python -- one of the following:

  - CPython_ : 3.6 and newer
  - PyPy_ : Latest 3.x version


Installation
------------

Package is uploaded on `PyPI <https://pypi.org/project/PyMySQL>`_.

You can install it with pip::

    $ python3 -m pip install PyQuickQuery

Documentation
-------------

Documentation is available online: https://pymysql.readthedocs.io/

For support, please refer to the `StackOverflow
<https://stackoverflow.com/questions/tagged/pymysql>`_.


Example
-------

The following examples make use of a simple table

.. code:: python
    
    import pyquickquery
    import pymysql # sqlite3 or postgres
    

    # Connect to the database
    query = pyquickquery.Query(pymysql.connect(host='localhost',
                                               user='user',
                                               password='password',
                                               database='db')
    
    # Create user in special table     
    query.create('users', {
      "login" : "josh1990"
      "password" : "012345"
    })
    # Returns ('1', 'josh1990')
    
    # Select first user     
    query.select('users', ['id', 'login']).first()
    # Returns ('1', 'josh1990')
    
    # Update user's data
    query.update('users', {
      "login" : "josh1990"
      "password" : "012345"
    }).where({ 'id' : 1 })




License
-------

PyQuickQuery is released under the MIT License. See LICENSE for more information.
