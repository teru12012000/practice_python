from flask import Flask
'''初期化処理を書いていく'''
app=Flask(__name__)
import flaskr.main

from flaskr import db
db.create_books_table()