def get_repair_response(my_bot, userText):
    msgAfterWait = ''
    milisecond = 0
    output = None

    if 'hỏng' in userText or 'không chạy' in userText or \
            'không hoạt động' in userText or 'đơ' in userText \
            or 'chạy chậm' in userText or 'yếu' in userText:
        output = 'thong_tin'
    elif 'thay' in userText or 'mua mới' in userText:
        output = 'thay_the'
    elif 'sửa' in userText:
        output = 'sua_chua'

    return {'output': str(my_bot.get_response(output)),
            'timeOut': {'msgAfterWait': msgAfterWait, 'milisecond': milisecond}} if output else None
