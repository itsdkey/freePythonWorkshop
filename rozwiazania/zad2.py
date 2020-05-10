# 1
print('########### Punkt 1 ###########')
user_var = input('podaj jakas wartosc: ')
print(f'podales wartosc: {user_var}')


# 2
print('########### Punkt 2 ###########')
first = input('podaj pierwsza liczbe calkowita: ')
second = input('podaj druga liczbe calkowita: ')

first = int(first)
second = int(second)

result = first + second
print(f'a) suma tych dwoch liczb wynosi: {result}')
result = first - second
print(f'b) {first} - {second} wynosi: {result}')
result = first * second
print(f'c) iloczyn wynosi: {result}')
result = first / second
print(f'd) iloraz wynosi: {result}')


# 3
print('########### Punkt 3 ###########')
first = 333
second = 27
result = first % second
print(f'{first=}, {second=}')
print(f'a) reszta z dzielenia wynosi: {result}')
result = first // second
print(f'b) iloraz z dzielenia wynosi: {result}')


# 4
from decimal import (
    ROUND_05UP,
    ROUND_CEILING,
    ROUND_DOWN,
    ROUND_FLOOR,
    ROUND_HALF_DOWN,
    ROUND_HALF_EVEN,
    ROUND_HALF_UP,
    ROUND_UP,
    Decimal
)
print('########### Punkt 4 ###########')
first = Decimal('20.75')
second = Decimal('11')
print(f'{first=}, {second=}')
print(f'dokładniejsza precyzja dzielenia: {Decimal(first / second)}')
result = Decimal(first / second).quantize(Decimal('0.00'), ROUND_HALF_UP)
print(f'a) {result=}')
result = Decimal(first / second).quantize(Decimal('0.00'), ROUND_DOWN)
print(f'b) {result=}')
result = Decimal(first / second).quantize(Decimal('0.00'), ROUND_UP)
print(f'c) {result=}')


print(f'*) {Decimal(first / second).quantize(Decimal("0.00"), ROUND_05UP)=}')
print(f'*) {Decimal(first / second).quantize(Decimal("0.00"), ROUND_CEILING)=}')
print(f'*) {Decimal(first / second).quantize(Decimal("0.00"), ROUND_FLOOR)=}')
print(f'*) {Decimal(first / second).quantize(Decimal("0.00"), ROUND_HALF_DOWN)=}')
print(f'*) {Decimal(first / second).quantize(Decimal("0.00"), ROUND_HALF_EVEN)=}')
