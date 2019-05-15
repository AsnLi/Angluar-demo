#coding=utf-8
from flask import Flask, abort, request, jsonify
from flask_cors import *  # 导入模块s
from books import books
from db import dbconn

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.before_request
def before_request():
    con = dbconn.connection
    try:
        con.ping()
    except Exception as e:
        con.reconnect()
        print(e)

app.register_blueprint(books, url_prefix='/books')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
