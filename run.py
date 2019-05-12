#coding=utf-8
from flask import Flask, abort, request, jsonify
from flask_cors import *  # 导入模块
from db import dbconn

app = Flask(__name__)
CORS(app, supports_credentials=True)
tasks = []

@app.route('/getTask', methods=['GET'])
def get_task():
    query = request.args
    if not query or 'id' not in query:
        rows = dbconn.fetch_rows(
            table='js_books',
            limit='0,5')
        return jsonify(rows)
    else:
        task_id = request.args['id']
        task = list(filter(lambda t: t['id'] == int(task_id), tasks))
        return jsonify(back_res(200, task, '成功')) if task else jsonify(back_res())

@app.route('/addTask/', methods=['POST'])
def add_task():
    query = request.json
    if not query or 'id' not in query or 'info' not in query:
        abort(400)

    task = {
        'id': query['id'],
        'info': query['info']
    }

    tasks.append(task)
    return jsonify(back_res(200, 1, '成功'))

def back_res(code = 0, data = [], msg = ''):
    return {
        "ResponseCode": code,
        "Data": data,
        "ResponseMessage": msg
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
