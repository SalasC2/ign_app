import flask
app = flask.Flask(__name__)
import mysql.connector

from app import routes

mydb = mysql.connector.connect(user='root', password='root', host='localhost', port=8889)

cursor = mydb.cursor()

