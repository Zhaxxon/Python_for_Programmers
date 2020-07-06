from collections import namedtuple

# Parts = namedtuple('Parts', 'id_num desc cost amount')
# auto_parts = Parts(id_num='1234', desc='Ford Engine', cost=1200.00, amount=10)
# print(auto_parts.id_num)

# auto_parts = ('1234', 'Ford Engine', 1200.00, 10)
# print(auto_parts[2]) # access the cost
# 1200.00

id_num, desc, cost, amount = auto_parts
# print(id_num)

Parts = {'id_num': '1234', 'desc': 'Ford Engine', 'cost': 1200.00, 'amount': 10}
# parts = namedtuple('Parts', Parts.keys())(**Parts)
parts = namedtuple('Parts', Parts.keys())
print (parts)
# <class '__main__.Parts'>

auto_parts = parts(**Parts)
print (auto_parts)
# Parts(amount=10, cost=1200.0, id_num='1234', desc='Ford Engine')