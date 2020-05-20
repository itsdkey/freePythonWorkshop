"""
        Zadania

1. Stwórz funkcję, która przyjmie dwa parametry i zwróci sumę.
"""


def sum_two_values(a, b):
    return a + b


print(sum_two_values(1, 2))

"""
2. Stwórz funkcję, która przyjmie dwie liczby całkowite i trzecią opcjonalną. Zwróc sumę tych 3ch wartości.
"""


def sum_three_values(a, b, c=0):
    return sum([a, b, c])


print(sum_three_values(2, 3))
print(sum_three_values(2, 3, 10))

"""
3. Stwórz funkcję, która przyjmie opcjonalną listę i dodaj do niej element '1'. Zwróć listę.
"""


# to jest niepoprawne ponieważ 'pusta' lista będzie aktualizowana jeśli znów wywołamy funkcje bez listy
# zadanie mialo na celu zwrócenie na to uwagi
# dzieje się tak ze względu, że listy są mutable - czyli zmienne. Nie powinno się ustawiać zmiennych typów danych jako
# domyślne parametry.
def append_list(local_list=[]):
    local_list.append(1)
    return local_list


print('# opcja 1')
print(append_list())
print(append_list([1, 2, 3]))
print(append_list())  # tu zwroci nam [1, 1] mimo, że funkcja wyglada jakby przyjmowala opcjonalną pustą listę
print(append_list([]))  # tu zwróci nam [1] ponieważ przekazaliśmy jawnie pustą listę


# poprawne wykonanie w tym wypadku
def append_list(local_list=None):
    local_list = local_list or []
    local_list.append(1)
    return local_list


print('# opcja 2')
print(append_list())
print(append_list([1, 2, 3]))
print(append_list())
print(append_list([]))


# lub z if'em
def append_list_with_if(local_list=None):
    if local_list is None:
        local_list = []
    local_list.append(1)
    return local_list


print('# opcja 3')
print(append_list_with_if())
print(append_list_with_if([1, 2, 3]))
print(append_list_with_if())
print(append_list_with_if([]))
"""
4. Stwórz program bazujący na dwóch funkcjach. Jedna funkcja powinna zawierać pobranie wartości. 
Druga funkcja powinna zawierać potęgowanie wartości podanej przez użytkownika.
Zakładamy, że użytkownik poda liczby całkowite.
Pierwsza funkcja powinna wywoływać drugą a wynik zapisywać do zmiennej lokalnej.
Druga funkcja powinna przyjąć dwa parametry: a - wartość podana przez użytkownika, b - liczbę, do której potęgi podnieść daną wartość
W przypadku gdy uzytkownik poda liczbę parzystą chcemy podnieść do 2-giej potęgi
W przypadku gdy użytkownik poda liczbę nieparzystą, chcemy podnieść tą wartość do 3-ciej potęgi.
Na konieć zwróć wynik.
"""


def power_value(a, b):
    return a ** b


def power_value_from_user():
    value = input('podaj liczbę: ')
    value = int(value)
    if value % 2 == 0:
        return power_value(value, 2)
    else:
        return power_value(value, 3)


for i in range(2):
    value = power_value_from_user()
    print(f'wynik: {value}')
