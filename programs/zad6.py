print("########## Punkt 1 ##########")
temp = {'temp': 1, 2: 3, 'klucz': [1, 2, 3], 'slownik': {'temp': 1}}
print(temp)


print("########## Punkt 2 ##########")
temp = {}
for i in range(3):
    key_and_value = input('podaj klucz i wartosc (klucz wartosc): ')
    key, value = key_and_value.split(' ')
    temp[key] = value
print(temp)


print("########## Punkt 3 ##########")
temp = {}
for i in range(3):
    key_and_value = input('podaj klucz i wartosc (klucz wartosc): ')
    key, value = key_and_value.split(' ')
    if key in temp:
        temp[key].append(value)
    else:
        temp[key] = [value]
print(temp)


print("########## Punkt 4 ##########")
first = {'temp': 1, 2: 3, 'klucz': 'wartosc'}
second = {'temp': 'test', 33: 'wartosc2'}
third = {**first, **second}
print(third)


print("########## Punkt 5 ##########")
from datetime import datetime
today = datetime.now()
day = today.weekday()
print(f'{today=}, weekday: {day}')
days = {
    0: 'poniedzialek',
    1: 'wtorek',
    2: 'środa',
    3: 'czwartek',
    4: 'piątek',
    5: 'sobota',
    6: 'niedziela',
}
print(days[day])
