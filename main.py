from values import Values


v = Values()

v.create('money', 1000, 1)

v.trade('buy', 'milk', 11, 4.1, 'money')
v.trade('buy', 'milk', 37, 7.5, 'money')
v.trade('buy', 'milk', 21, 4.2, 'money')
v.trade('buy', 'milk', 33, 7.1, 'money')
v.trade('buy', 'milk', 7, 8.2, 'money')
v.trade('buy', 'milk', 14, 10.2, 'money')

v.trade('sell', 'milk', 11, 8.4, 'money')
v.trade('sell', 'milk', 17, 9.1, 'money')

# v.trade('buy', 'milk', 19, 5.1, 'money')
v.trade('sell', 'milk', 4, 7.9, 'money')
v.trade('sell', 'milk', 4, 4.6, 'money')
v.trade('sell', 'milk', 30, 8.3, 'money')

v.trade('buy', 'corn', 11, 3, 'milk')
# v.trade('buy', 'milk', 3, 3, 'corn')

# v.trade('sell', 'corn', 11, 22, 'money')


print(v.get_res())

print(v.get_financial_result())

print(v.get_assets())