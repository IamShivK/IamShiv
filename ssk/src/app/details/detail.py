from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'shiv95'
app.config['MYSQL_DB'] = 'company'

mysql = MySQL(app)
@app.route('/users')
def users():
    cur=mysql.connection.cursor()
    users = cur.execute("SELECT * FROM company.logins")
