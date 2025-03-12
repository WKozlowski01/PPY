# Zadanie 1 (1 pkt)
# Napisz program, który powinien:
# Zawierać listę wyników testów kilku uczniów, gdzie każdy wynik jest reprezentowany przez słownik zawierający:
# name (string): imię ucznia,
# scores (lista): lista wyników ucznia z poszczególnych testów (np. [78, 92, 85]).
from turtledemo.paint import switchupdown

from unicodedata import numeric

studenci = {
    "Ania": [101,75,33],
    "Kasia" : [76,55,12],
    "Bartek" : [65,55,60],
    "Marek" : [23,80,98]
}

# Sprawdź czy każdy wynik nie jest większy od 100, jeżeli jest to usuń go z listy.
for key, value in studenci.items():
    for x in value:
        if x >100: studenci[key].remove(x)

print(studenci)

# Stworz zmienną average_score, która będzie słownikiem:
# klucz: imię ucznia,
# wartość: średnia uzyskana przez ucznia, która jest liczbą całkowitą.
avg =0
average_score = dict()
for key, value in studenci.items():
    for x in value:
       avg += x
    avg = avg / len(value)
    average_score.update({key:avg})
    avg = 0

print(average_score)

# Wypisz w terminalu, który uczeń miał najwyższą średnia i jak to była średnia w następujący sposób:\
# "Najwyższą średnią uzyskał/ła [imie] , która wynosiła [średnia]“.
max_avg=0
max_name =""
for key, value in average_score.items():
    if average_score.get(key) > max_avg:
        max_avg = average_score.get(key)
        max_name = key
print("Najwyższą średnią uzyskał/ła" , max_name, "która wynosiła ",max_avg)


# Zadanie 2 (0,5 pkt)
# Napisz kod, który wyświetli słowa z listy, które są ,,podobne" do napisu s
# w tym sensie, że składające się z tych samych znaków — ale ewentualnie występujących inną liczbę razy.
#
# #PRZYKŁAD
# s = 'one'
# lista = ['one', 'two', 'none', 'three', 'neon', 'eon']
# >> none neon eon

s = 'one'
lista = ['one', 'two', 'none', 'three', 'neon', 'eon']

for i in lista:
    tmp = set(i)
    if (set(i) == set(s)) and (i!=s):
        print(i)

# Zadanie 3 (1,5 pkt)
# Napisz program, który umożliwia zarządzanie książką adresową. Program powinien umożliwiać użytkownikowi wykonywanie następujących operacji:
#
# Dodawanie nowego kontaktu do książki adresowej.
# Wyświetlanie wszystkich kontaktów z książki adresowej.
# Wyszukiwanie kontaktu po nazwie i wyświetlanie szczegółów.
# Usuwanie kontaktu z książki adresowej.
#
# Użyj słownika, gdzie kluczem będzie nazwa kontaktu, a wartością będzie lista informacji o kontakcie (np. imię, nazwisko, numer telefonu).

ksiazka= {
    "Mama": ["Anna", "Kowalska", 123456789]
}

running = True
while running:
    print(
    1,"Dodawanie nowego kontaktu do książki adresowej\n",
    2, "Wyświetlanie wszystkich kontaktów z książki adresowej.\n",
    3,"Wyszukiwanie kontaktu po nazwie i wyświetlanie szczegółów.\n",
    4,"Usuwanie kontaktu z książki adresowej.\n")
    option  = input()
    if option == "1":
        print("podaj nazwe kontaktu ")
        nazwa = input()
        print("podaj imie")
        imie = input()
        print("podaj nazwisko")
        nazwisko = input()
        print("podaj numer telefonu")
        numer = int(input())
        ksiazka.update({nazwa:[imie,nazwisko,numer]})
    elif option == "2":
        print(ksiazka)
    elif option == "3":
        print("Podaj nazwe kontaktu")
        nazwa = input()
        if nazwa not in ksiazka.keys():
            print("nie ma takiego kontaktu")
        else:
            print(ksiazka.get(nazwa))
    elif option == "4":
        print("Podaj nazwe kontaktu")
        nazwa = input()
        if nazwa not in ksiazka.keys():
            print("nie ma takiego kontaktu")
        else:
            ksiazka.pop(nazwa)
    else: running = False









