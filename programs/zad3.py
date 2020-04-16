print('########### Punkt 1 ###########')
first = input('podaj pierwsza czesc zdania: ')
second = input('podaj druga czesc zdania: ')
result = first + second
print(f'{result}')
result = ' '.join([first, second])
print(f'{result=}')


print('########### Punkt 2 ###########')
sentence = input('podaj zdanie: ')
find = input('czego wyszukac? ')
replace_with = input('czym zastapic? ')
result = sentence.replace(find, replace_with)
print(f'{result=}')
