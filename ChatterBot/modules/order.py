import json
from random import randint


def customerInfo(info):
    key = info
    if info == 'name':
        key = 'save_name'
    elif info == 'phone':
        key = 'save_phone'
    elif info == 'address':
        key = 'save_address'
    elif info == 'product':
        key = 'save_product_link'
    return key


def saveUserInfo(cache):
    file = open('data/learned//userInfo.json', 'r', encoding='utf-8-sig')
    userInfo = json.load(file)
    for e in cache:
        userInfo[e] = cache[e]
    file = open('data/learned//userInfo.json', 'w', encoding='utf-8-sig')
    json.dump(userInfo, file, indent=2, ensure_ascii=False)
    file.close()


def linkOrder(my_bot):
    order = str(my_bot.get_response('confirm_order'))
    file = open('data/orderInfo.json', 'r', encoding='utf-8-sig')
    data = json.load(file)
    file.close()
    data = data[len(data) - 1]
    order = order.replace('!id!', data['id'])
    order = order.replace('!product!', data['product'])
    order = order.replace('!name!', data['name'])
    order = order.replace('!phone!', str(data['phone']))
    order = order.replace('!address!', data['address'])
    return order


def changePersonal():
    file = open('data/orderInfo.json', 'r', encoding='utf-8-sig')
    data = json.load(file)
    if len(data) > 0:
        change = data[len(data) - 1]
        for e in change:
            if e != 'product' and e != 'id':
                data[len(data) - 1][e] = ''
        file = open('data/orderInfo.json', 'w', encoding='utf-8-sig')
        json.dump(data, file, indent=2, ensure_ascii=False)
        file.close()

    return customerInfo(checkOrderInfo())


def newOrder():
    file = open('data/orderInfo.json', 'r', encoding='utf-8-sig')
    data = json.load(file)
    cache = open('data/learned//userInfo.json', 'r', encoding='utf-8-sig')
    userInfo = json.load(cache)

    new = {
        "id": str(randint(10, 99)) + ":" + str(randint(10000, 99999)),
        "product": "",
        "name": userInfo['name'],
        "phone": userInfo['phone'],
        "address": userInfo['address']
    }

    data.append(new)
    print(data)
    file = open('data/orderInfo.json', 'w', encoding='utf-8-sig')
    json.dump(data, file, indent=2, ensure_ascii=False)
    file.close()

    return customerInfo(checkOrderInfo())


def confirmOrder():
    file = open('data/orderInfo.json', 'r', encoding='utf-8-sig')
    data = json.load(file)
    if len(data) > 0:
        return 'order_confirmed'
    return 'unknown'


def checkOrderInfo():
    file = open('data/orderInfo.json', 'r', encoding='utf-8-sig')
    data = json.load(file)
    file.close()
    data = data[len(data) - 1]
    if len(data) == 0:
        return 'unknown'
    for e in data:
        if str(data[e]) == '':
            return e
    file = open('data/orderInfo.json', 'r', encoding='utf-8-sig')
    data = json.load(file)
    file.close()
    cache = {
        "name": data[len(data) - 1]['name'],
        "phone": data[len(data) - 1]['phone'],
        "address": data[len(data) - 1]['address']
    }
    saveUserInfo(cache)
    return 'confirm_order'


def cancelOrder():
    file = open('data/orderInfo.json', 'r', encoding='utf-8-sig')
    data = json.load(file)
    if len(data) > 0:
        del data[len(data) - 1]
        file = open('data/orderInfo.json', 'w', encoding='utf-8-sig')
        json.dump(data, file, indent=2)
        file.close()

    return 'order_canceled'


def proccessOrder(userText):
    output = 'unknown'
    if userText == '1':
        output = confirmOrder()
    elif userText == '2':
        output = cancelOrder()
    elif userText == '0':
        output = changePersonal()
    elif userText == '5':
        output = newOrder()
    elif userText == '7':
        output = 'order_end'

    return output
