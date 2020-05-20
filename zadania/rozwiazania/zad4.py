print('########## Punkt 1 ###########')
value = input('podaj liczbe calkowita: ')
value = int(value)
if value % 2 == 0:
    print('to jest liczba parzysta')
else:
    print('to jest liczba nieparzysta')


print('######### Punkt 2 ############')
first = input('podaj pierwsza liczbe calkowita: ')
second = input('podaj druga liczbe calkowita: ')
first = int(first)
second = int(second)
if first % second == 0:
    print(f'liczba {first} jest podzielna przez {second}')
elif second % first == 0:
    print(f'liczba {second} jest podzielna przez {first}')
else:
    print(f'liczby {first} i {second} nie są przez siebie podzielne')


print('########### Punkt 3 ############')
from datetime import datetime
today = datetime.now()
day = today.weekday()
print(f'{today=}, weekday: {day}')
if day == 0:
    print('poniedzialek')
elif day == 1:
    print('wtorek')
elif day == 2:
    print('środa')
elif day == 3:
    print('czwartek')
elif day == 4:
    print('piątek')
elif day == 5:
    print('sobota')
elif day == 6:
    print('niedziela')


print('######### Punkt 4 ############')
value = input('podaj pierwsza liczbe calkowita: ')
value = int(value)
if value % 3 == 0 and value % 5 == 0:
    print('liczba jest podzielna przez 3 i 5')
elif value % 2 == 0 or value % 7 == 0:
    print('liczba jest podzielna przez 2 lub 7')


print('######### Punkt 5 ############')
first = input('podaj pierwsza liczbe calkowita: ')
second = input('podaj druga liczbe calkowita: ')
third = input('podaj trzecia liczbe calkowita: ')
first = int(first)
second = int(second)
third = int(third)
if first % second == 0 and first % third == 0:
    print(f'liczba {first} jest podzielna przez {second} i {third}')
else:
    if first % second == 0:
        print(f'liczba {first} jest podzielna przez {second}')
    elif first % third == 0:
        print(f'liczba {first} jest podzielna przez {third}')
    else:
        print(f'liczba {first} nie jest podzielna ani przez {second} ani przez {third}')