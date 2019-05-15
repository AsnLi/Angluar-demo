#coding=utf-8
from flask import Blueprint, request, abort, jsonify
from response import back_res
from db import dbconn

books = Blueprint('/books',__name__)
tasks = []

@books.route('/getBooks', methods=['GET'])
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

@books.route('/addBooks/', methods=['POST'])
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