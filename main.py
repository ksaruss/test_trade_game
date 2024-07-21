from objects.company import Company


c1 = Company(1)

c1.create('money', 1000, 1)
print(c1.get_accounting())
c1.trade('buy', 'currency', 10, 10, 'money')
c1.trade('buy', 'milk', 7, 1, 'currency')
print(c1.get_accounting())
c1.trade('sell', 'currency', 2, 11, 'money')
c1.trade('buy', 'milk', 25, 5.5, 'money')
c1.trade('sell', 'milk', 5, 12, 'money')

print(c1.get_accounting())

# print(c1.get_list_resources())








