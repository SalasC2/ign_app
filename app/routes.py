from app import app
from flask import request, jsonify
import mysql.connector
import MySQLdb
import csv
import json
import os

conn = MySQLdb.connect(host=os.getenv("DB_HOST"), 
                    port=int(os.getenv("PORT")),
                    user = os.getenv("USERNAME"),
                    passwd = os.getenv("PASSWORD"),
                    db = os.getenv("DATABASE"))
cursor = conn.cursor()

@app.route("/getArticles", methods=["GET"])
def articles():
    cursor.execute('''select * from article''')
    r = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'Articles' : r})

@app.route("/getVideos", methods=["GET"])
def videos():
    cursor.execute('''select * from video''')
    r = [dict((cursor.description[i][0], value for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'Videos' : r}) 

@app.route("/getCategories", methods=["GET"])
def categories():
    cursor.execute('''select * from category''')
    r = [dict((cursor.description[i][0], value for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'Categories' : r})   


@app.route("/getArticlesByCategory/<string:category_type>") 
def category_articles(category_type):
    cursor.execute(""" SELECT * FROM article 
                        INNER JOIN category_article ON article.article_id = category_article.article_id 
                        INNER JOIN category ON category.category_id = category_article.category_id 
                        WHERE category_type = %s; """, [category_type])
    r = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'Articles by %s' % category_type: r})      


@app.route("/getVideosByCategory/<string:category_type>") 
def video_articles(category_type):
    cursor.execute(""" SELECT * FROM video 
                        INNER JOIN category_video ON video.video_id = category_video.video k_id 
                        INNER JOIN category ON category.category_id = category_video.category_id 
                        WHERE category_type = %s; """, [category_type])
    r = [dict((cursor.description[i][0], value)
           for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'Videos By %s' % category_type : r})   
       
