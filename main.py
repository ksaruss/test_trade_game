from values import Values
from objects.company import Company


c1 = Company(1)

c1.create('money', 1000)


print(c1.accounting.get_accounting_book())

print(c1.get_list_resources())








# v = Values()
#
# v.create('money', 1000, 1)
#
# v.trade('buy', 'corn', 100, 5, 'money')
# v.trade('buy', 'milk', 10, 3, 'corn')
# v.trade('sell', 'milk', 8, 21, 'money')
# v.trade('sell', 'corn', 70, 5.1, 'money')
# print(v.get_res())
#
# print(v.get_financial_result())
#
# print(v.get_assets())