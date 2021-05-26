# import json
#
# file = open('data/orderInfo.json', 'r', encoding='utf-8')
# data = json.load(file)
# new = {
#     "id": "",
#     "product": "",
#     "name": "",
#     "phone": "",
#     "address": ""
# }
# data.append(new)
# print(data)
# file = open('data/orderInfo.json', 'w', encoding='utf-8')
# json.dump(data, file, indent=2, ensure_ascii=False)
from pyvi import ViTokenizer, ViPosTagger, ViUtils

ViTokenizer.tokenize(u"Trường đại học bách khoa hà nội")

ViPosTagger.postagging(ViTokenizer.tokenize(u"Trường đại học Bách Khoa Hà Nội"))

ViUtils.remove_accents(u"Trường đại học bách khoa hà nội")

ViUtils.add_accents(u'truong dai hoc bach khoa ha noi')




