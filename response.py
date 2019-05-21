status = {
    "code": '',
    "message": 0
}

def set_status(code = 0, msg = ''):
    status["code"] = code
    status["message"] = msg
    print(status["code"])

def back_res(data = []):
    print(status["code"], 1111)
    return {
        "ResponseCode": status["code"],
        "Data": data,
        "ResponseMessage": status["message"]
    }