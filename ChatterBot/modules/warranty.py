import json
from datetime import date

from ChatterBot17.ChatterBot.modules.accessories_advisory import hasNumbers


def check_warranty_Date(str):
    today = date.today()
    today = today.strftime('%d/%m/%Y')
    list_today = today.split('/')

    listDateWarranty = [int(s) for s in str.split('/') if s.isdigit()]
    print(listDateWarranty)
    lengthWarranty = len(listDateWarranty)
    if 'năm ngoái' in str or 'hôm qua' in str or 'hôm kia' in str or 'hôm trước' in str \
            or 'tuần trước' in str or 'tuần trước' in str or 'tháng trước' in str:
        return True
    elif lengthWarranty == 0:
        return False
    else:
        if (int(list_today[2]) - listDateWarranty[2]) > 1:
            return False
        elif int(list_today[2]) - listDateWarranty[2] == 0:
            return True
        else:
            if (int(list_today[1]) - listDateWarranty[1]) > 0:
                return False
            elif (int(list_today[1]) - listDateWarranty[1]) < 0:
                return True
            else:
                if (int(list_today[0]) - listDateWarranty[0]) >= 0:
                    return False
                else:
                    return True


def check_in(output, str):
    listStr = str.split(' ')
    for i in listStr:
        if output == i:
            return True
    return False


def getData_InforLaptop():
    with open('data/bill.json', 'r', encoding="utf-8-sig") as bill_file:
        reader_loader = json.load(bill_file)
    size = len(reader_loader["value_bill"])
    listSerial = []
    listPrice = []
    listName = []
    listDateBuy = []
    listNameCustomer = []
    listAll = []
    for i in range(0, size):
        listSerial.append(reader_loader["value_bill"][i]["serial"])
        listPrice.append(reader_loader["value_bill"][i]["price"])
        listName.append(reader_loader["value_bill"][i]["nameLaptop"])
        listDateBuy.append(reader_loader["value_bill"][i]["dateBuy"])
        listNameCustomer.append(reader_loader["value_bill"][i]["nameCustomer"])

    listAll.append(listSerial)
    listAll.append(listPrice)
    listAll.append(listName)
    listAll.append(listDateBuy)
    listAll.append(listNameCustomer)

    return listAll


def check_Warranty_Serial(userText):
    listAll = getData_InforLaptop()
    listSerial = listAll[0]

    size = len(listSerial)
    for i in range(0, size):
        if listSerial[i] in userText:
            return True
    return False


def get_InforLaptop_serial(userText):
    listAll = getData_InforLaptop()
    listSerial = listAll[0]
    listPrice = listAll[1]
    listName = listAll[2]
    listDateBuy = listAll[3]
    listNameCustomer = listAll[4]
    listInforLap = []

    size = len(listSerial)
    for i in range(0, size):
        if listSerial[i] in userText:
            listInforLap.append(listSerial[i])
            listInforLap.append(listPrice[i])
            listInforLap.append(listName[i])
            listInforLap.append(listDateBuy[i])
            listInforLap.append(listNameCustomer[i])
            return listInforLap
    return "ko có gì cả"


def get_warranty_response(my_bot, request):
    userText = request.args.get('msg')

    userText = str.lower(userText)
    timeOut = 0
    output = None
    msgAfterWait = ''

    if 'bảo hành' in userText or 'kiểm tra' in userText or "hết hạn" in userText:
        output = 'kiểm tra bảo hành'
    elif check_Warranty_Serial(userText):
        listInfor = get_InforLaptop_serial(userText)
        respon = "Sản phẩm " + listInfor[2] + "(mã sản phẩm: " + listInfor[0] + ") " + \
                 "của khách hàng " + listInfor[4] + " được mua vào ngày " + listInfor[3]

        if check_warranty_Date(listInfor[3]):
            output = "vẫn còn thời hạn bảo hành"
            res = str(my_bot.get_response(output))
            respon = respon + ' vẫn còn thời hạn bảo hành. '
            return {'output': respon + res, 'timeOut': {'msg': msgAfterWait, 'milisecond': timeOut}}
        else:
            output = 'hết hạn bảo hành'
            respon = respon + " đã hết hạn bảo hành. "
            res = str(my_bot.get_response(output))
            return {'output': respon + res, 'timeOut': {'msg': msgAfterWait, 'milisecond': timeOut}}
    elif not check_Warranty_Serial(userText) and hasNumbers(userText) and 'hd' in userText:
        output = 'ko trùng serial'
    if 'thay thế' in userText or 'sửa chữa' in userText:
        output = None

    return {'output': str(my_bot.get_response(output)),
            'timeOut': {'msg': msgAfterWait, 'milisecond': timeOut}} if output else None
