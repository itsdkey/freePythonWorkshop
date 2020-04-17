print("########## Punkt 1 ##########")
temp = [1, 2, 3]
print(temp)


print("########## Punkt 2 ##########")
temp = [1, 2, 3]
index = 0
for value in temp:  # enumerate
    print(f'{index}: {value}')
    index += 1


print("########## Punkt 3 ##########")
first = [1, 2, 3, 4]
second = [1, 5, 6, 7]
result = first + second
print(result)


print("########## Punkt 4 ##########")
temp = [i for i in range(10)]
print(f'a) {temp[2]}, {temp[3]}, {temp[6]}')
print(f'b) {temp[:3]}')
print(f'c) {temp[3:8]}')
print(f'd) {temp[7:]}')  # print(f'd) {temp[-3:]}')
print(f'e) {temp[::2]}')


print("########## Punkt 5 ##########")
size = input('podaj wielkosc listy: ')
size = int(size)
my_list = []
for i in range(size):
    value = input('podaj jakas wartosc: ')
    my_list.append(value)
print(my_list)
print(my_list[-3:])


print("########## Punkt 6 ##########")
first = [1, 2, 33, 48, 22, 4, 5, 6, 100, 1, 2, 44, 44]
second = [1, 2, 3]
result = []
for value in second:
    if value in first:
        first.remove(value)
print(first)
