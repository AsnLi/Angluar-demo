import json

status = {
    "code": '',
    "message": 0
}

def set_status(code = 0, msg = ''):
    status["code"] = code
    status["message"] = msg
    # print(status["code"])

def check_json_format(raw_msg):
     if isinstance(raw_msg, str):  # 首先判断变量是否为字符串
        try:
            json.loads(raw_msg, encoding='utf-8')
        except ValueError:
            return False

        return True
     else:
        return False

def back_res(data = {}):
    for item in data['rows']:
        for val in item:
            tmp = item[val]
            if(check_json_format(tmp)):
                item[val] = json.loads(tmp)

    return data
    # print(status["code"], 1111)
    # return {
    #     "ResponseCode": status["code"],
    #     "Data": data,
    #     "ResponseMessage": status["message"]
    # }

