from decimal import Decimal

temp = None
print(f'{temp=}')

active = True
inactive = False
print(f'{active=}, {inactive=}')

my_variable = 10
print(f'{my_variable=}')

amount = 10.23
amount_in_decimal = Decimal('2.55')
print(f'{amount=}, {amount_in_decimal=}')

sentence = 'to jest super zdanie'
print(f'{sentence=}')

my_list = [1, 2, 3, 4, True, False, None, inactive]
print(f'{my_list=}')

my_dict = {1: my_list, 'temp': 'test', 2: 3}
print(f'{my_dict=}')
