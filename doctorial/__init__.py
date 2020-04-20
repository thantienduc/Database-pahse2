import mysql.connector
from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
'''
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#app.config['MYSQL_PORT'] = 80
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'Test_flask'

mysql = MySQL(app)
'''
cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='Test_flask')

from doctorial import routes

