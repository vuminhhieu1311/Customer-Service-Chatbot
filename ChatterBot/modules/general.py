from datetime import date, timedelta


def get_general_response(my_bot, userText):
    output = None
    msgAfterWait = ''
    milisecond = 0
    if 'chào' in userText:
        output = 'xin chào'
        output = str(my_bot.get_response(output))
    if 'tạm biệt' in userText:
        output = 'tạm_biệt'
        output = str(my_bot.get_response(output))
    elif 'địa chỉ' in userText or ('cửa hàng' in userText and ('ở đâu' in userText or 'đến' in userText)) \
            or 'ở đâu' in userText:
        output = 'địa_chỉ'
        output = str(my_bot.get_response(output))
    elif 'cám ơn' in userText or 'cảm ơn' in userText or 'thanks' in userText:
        output = 'cám_ơn'
        output = str(my_bot.get_response(output))
    elif 'ưu đãi' in userText or 'sale' in userText or 'khuyến mãi' in userText \
            or 'chương trình' in userText or 'giảm giá' in userText:
        output = 'ưu đãi'
        today = date.today()
        offset = (today.weekday() - 2) % 7
        sale_start = today - timedelta(days=offset)
        sale_end = today + timedelta(7)
        output = str(my_bot.get_response(output)).replace('!sale_start!', str(sale_start)).replace('!sale_end!',
                                                                                                   str(sale_end))
    elif 'rồi' in userText or 'chọn được' in userText:
        output = 'chọn_được'
        output = str(my_bot.get_response(output))
    elif ('mua' in userText and 'online' in userText) or 'đặt' in userText:
        output = 'begin_order'
        output = str(my_bot.get_response(output))
    elif 'mua' in userText and ('trực tiếp' in userText or ('tại' in userText and 'cửa hàng' in userText)):
        output = 'mua_trực_tiếp'
        output = str(my_bot.get_response(output))
    return {"output": output, 'timeOut': {'msg': msgAfterWait,
                                          'milisecond': milisecond}} if output else None
