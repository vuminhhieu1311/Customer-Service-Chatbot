import json
import re


def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))


def accessories_link(my_bot, type, brand, model):
    file = open('data/accessories.json')
    data = json.load(file)
    file.close()

    if model:
        response = str(my_bot.get_response("model_phụ_kiện"))
    elif brand == 'common':
        response = str(my_bot.get_response('loại_phụ_kiện'))
    else:
        response = str(my_bot.get_response('hãng_phụ_kiện'))
    response = response.replace('!type!', type.upper())
    link = '<a href="' + data[type][
        model if model else brand] + '" target="_blank">' + type.upper() + (
               '' if (brand == 'common' and not model) else ' ' + model.upper() if model else brand.upper()) + '</a>'
    response = response.replace('!link!', link)
    if '!brand!' in response:
        response = response.replace('!brand!', brand.upper())
    if '!model!' in response and model:
        response = response.replace('!model!', model.upper())
    if '!list' in response:
        file = open('data/learned/accessories_learned.json')
        data = json.load(file)
        keys = list(data[type])
        for e in keys:
            if int(data[type][e]) < 2:
                keys.remove(e)
        choices = str(keys).replace("'", '')
        choices = choices.replace('[', '')
        choices = choices.replace(']', '')
        choices = choices.replace('common,', '')
        response = response.replace('!list!', choices.upper())

    print(response)
    return response


def accessories_analyze(my_bot, userText):
    file = open('data/accessories.json')
    data = json.load(file)
    file.close()

    type = ''
    brand = 'common'
    model = None
    if 'ram' in userText:
        type = 'ram'
    elif 'ssd' in userText:
        type = 'ssd'
    elif 'hdd' in userText:
        type = 'hdd'
    elif 'vga' in userText or 'màn' in userText:
        type = 'vga'
    elif 'sạc' in userText or 'adapter' in userText:
        type = 'adapter'
    elif 'ổ cứng' in userText:
        type = 'hdd'
    elif 'cpu' in userText or 'chip' in userText:
        type = 'cpu'
    for e in data:
        if e in userText:
            type = e
    for e in data[type]:
        if e in userText and not hasNumbers(e):
            brand = e
        if e in userText and hasNumbers(e):
            model = e
    return accessories_link(my_bot, type, brand, model)


def laptop_link(my_bot, feature, choice):
    with open('data/laptop_features.json',
              encoding='utf-8-sig') as file:
        data = json.load(file)
    file.close()

    output = None
    if choice:
        output = str(my_bot.get_response('laptop_features'))
        output = output.replace('!feature!', ((feature if feature != 'screen' else 'màn hình') + ' ' + choice).upper())
        link = '<a href="' + data[feature][choice] + '" target="_blank">Click here</a>'
        output = output.replace('!link!', link)

    return output


def laptop_analyze(my_bot, userText):
    with open('data/laptop_features.json', encoding='utf-8-sig') as file:
        data = json.load(file)
    file.close()

    feature = None
    choice = None
    if 'ram' in userText:
        feature = 'ram'
    if 'cpu' in userText or 'core' in userText or 'chip' in userText:
        feature = 'core'
    if 'ssd' in userText:
        feature = 'ssd'
    if 'màn' in userText or 'inch' in userText:
        feature = 'screen'
    for e in data:
        if e in userText:
            feature = e
    for e in data[feature]:
        if e in userText:
            choice = e
            break
    return laptop_link(my_bot, feature, choice)


def get_accessories_response(my_bot, userText):
    msgAfterWait = 'Bạn đã chọn được mẫu nào chưa ạ.'
    miliseconds = 5000
    output = None
    if 'phụ kiện' in userText:
        output = my_bot.get_response('phụ_kiện')
    if 'ram' in userText or 'cpu' in userText or 'chip' in userText or 'core' in userText \
            or 'sạc' in userText or 'ổ cứng' in userText \
            or 'hdd' in userText or 'ssd' in userText or 'vga' in userText \
            or 'adapter' in userText or 'màn' in userText or 'màu' in userText:
        if 'laptop' in userText or 'máy' in userText or 'lap' in userText:
            output = laptop_analyze(my_bot, userText)
        else:
            output = accessories_analyze(my_bot, userText)
    return {"output": str(output), 'timeOut': {'msg': msgAfterWait,
                                               'milisecond': miliseconds}} if output else None
