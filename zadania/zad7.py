"""
        Temat 7: funkcje

Przykłady
1. Stworzenie funkcji z dwoma wymaganymi parametrami
"""


def foo(a, b):
    print("funkcja foo")
    print(a, b)


foo(1, 'test')


"""
2. Stworzenie funkcji z domyślnym parametrem.
"""


def foo2(a='test'):
    print("funkcja foo2")
    print(a)


foo2()
foo2(1)
foo2(a='nowy tekst')


"""
3. Stworzenie funkcji z różna ilością parametrów bez nazwy - *args
args - jest to skrót od arguments. Pozwala na przekazanie różnej liczby parametrów pozycyjnych.
Aby parametr trafił do tej tupli należy go przekazać bez podania nazwy pod jaki parametr ma trafić
"""


def foo_with_args(param1, *args):
    print("funkcja foo_with_args")
    print(param1)
    print(args)


foo_with_args(1)
foo_with_args(1, 2, 3, 4, 5)
foo_with_args(1, 2)


"""
4. Stworzenie funkcji z różną ilością parametrów nazwanych - **kwargs.
kwargs - jest to skrót od keyword arguments. Pozwala na przekazanie różnej liczby parametrów nazwanych (więc takich
gdzie kolejność można mieszać, bo program będzie wiedział pod jaki parametr go przekazać.
"""


def foo_with_kwargs(param1, param2='test', **kwargs):
    print("funkcja foo_with_kwargs")
    print(param1, param2)
    print(kwargs)


foo_with_kwargs(1)
foo_with_kwargs(1, 'test2')
foo_with_kwargs(1, param2='test2', param3=12, param4=36)
foo_with_kwargs(1, param3='to jest test', param2='to jest drugi parametr')
foo_with_kwargs(1, param3='to jest test', test='to jest dodatkowy parametr')


"""
        Zadania

1. Stwórz funkcję, która przyjmie dwa parametry i zwróci sumę.
"""


"""
2. Stwórz funkcję, która przyjmie dwie liczby całkowite i trzecią opcjonalną. Zwróc sumę tych 3ch wartości.
"""


"""
3. Stwórz funkcję, która przyjmie opcjonalną listę i dodaj do niej element '1'. Zwróć listę.
"""


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