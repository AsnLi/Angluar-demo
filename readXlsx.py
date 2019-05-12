import xlrd
from db import dbconn

data = xlrd.open_workbook('test11.xlsx')
table = data.sheets()[0]
values = [
    'title', 'author', 'column', 'code', 'date',
    'count', 'abstract', 'views', 'press',
    'borrows','tags','keywords','directory'
]

for i in range(table.nrows):
    if(i != 0):
        item = table.row_values(i)
        obj = {}
        for index in range(len(item)):
            obj[values[index]] = item[index]
        dbconn.insert(table='js_books', data=obj)
        print('ok')

