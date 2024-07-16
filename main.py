from values import Values


v = Values()

v.create('money', 1000, 1)

v.trade('buy', 'milk', 11, 4.1, 'money')
v.trade('buy', 'milk', 37, 7.5, 'money')
v.trade('buy', 'milk', 21, 4.2, 'money')
v.trade('buy', 'milk', 33, 7.1, 'money')
v.trade('buy', 'milk', 7, 8.2, 'money')
v.trade('buy', 'milk', 14, 10.2, 'money')

v.trade('sell', 'milk', 13, 8.4, 'money')
v.trade('sell', 'milk', 17, 9.1, 'money')
v.trade('sell', 'milk', 4, 7.9, 'money')

v.trade('buy', 'corn', 11, 3, 'milk')
v.trade('buy', 'milk', 3, 4, 'corn')

print(v.get_res())

