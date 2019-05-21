# encoding: utf-8

from flask import Blueprint, request, abort, jsonify
from response import back_res
from db import dbconn

books = Blueprint('/books',__name__)
table_name = 'js_books'

@books.route('/getBooks', methods=['POST'])
def get_books():
    query = request.json #默认值判断
    index = query['pageIndex']
    size = query['pageSize']

    if 'filter' not in query:
        rows = dbconn.fetch_rows(
            table=table_name,
            limit=','.join([str((index - 1)*size), str(size)])
        )
        return jsonify(back_res({
            "rows": rows,
            "total": dbconn.count(table=table_name)
        }))
    else:
        filter = query['filter']
        order = filter.pop('order')

        rows = dbconn.fetch_rows(
            table=table_name,
            condition=filter,
            order=order,
            limit=','.join([str((index - 1)*size), str(size)])
        )
        return jsonify(back_res({
            "rows": rows,
            "total": dbconn.count(table=table_name, condition=filter)
        }))
        # return jsonify(back_res(200, task, '成功')) if task else jsonify(back_res())

@books.route('/addBooks/', methods=['POST'])
def add_books():
    query = request.json
    # if not query or 'title' not in query or 'code' not in query:
    #     abort(400)

    last_id = dbconn.insert(table=table_name, data=query)
    return jsonify(back_res(last_id))

@books.route('/uptBooks/', methods=['POST'])
def upt_books():
    query = request.json

    rows = dbconn.update(table=table_name, data=query['data'], condition=query['condition'])
    return jsonify(back_res(rows))

@books.route('/delBooks/', methods=['POST'])
def del_books():
    query = request.json

    rows = dbconn.delete(table=table_name, condition=query, limit='1')
    return jsonify(back_res(rows))