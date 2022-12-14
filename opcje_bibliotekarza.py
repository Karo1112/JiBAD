import csv


def zwrot_ksiazki():
    tablica = []
    with open('wypozyczenia.csv', 'r', newline='') as oddaj:
        tytul = str(input("Podaj tytuł książki, którą chcesz zwrócić: "))
        csvreader = csv.reader(oddaj, delimiter=',')
        for row in csvreader:
            tablica.append(row)

    for items in tablica:
        for item in items:
            if tytul.lower() in item.lower():
                items[1] = '-'
                items[2] = 'NIE'
                items[4] = 'NIE'

    with open('wypozyczenia.csv', 'w', newline='') as wypozycz:
        csvwriter = csv.writer(wypozycz, delimiter=',')
        for item in tablica:
            csvwriter.writerow(item)
        print("Udało ci się zwrócić książkę.")


def dodaj_ksiazke():
    with open('katalog.csv', 'a', newline='') as dodaj:
        csvwriter = csv.writer(dodaj)
        tytul = str(input("Podaj tytuł: "))
        autor = str(input("Podaj autora: "))
        slowa = str(input("Podaj slowa kluczowe: "))
        ksiazka = [tytul, autor, slowa]
        csvwriter.writerow(ksiazka)
        print("Udalo ci sie dodać książkę.")
    with open('katalog.csv', 'r', newline='') as lista:
        reader = csv.reader(lista, delimiter=',')
        for row in reader:
            print(row)
    with open('wypozyczenia.csv', 'a', newline='') as wyp:
        csvwriter = csv.writer(wyp, delimiter=',')
        csvwriter.writerow([tytul, '-', 'NIE', 'NIE', 'NIE'])


def usun_ksiazke():
    tytul = str(input("Podaj tytuł książki, którą chcesz usunąć: "))
    tablica = []
    tablica1 = []

    with open('katalog.csv', 'r', newline='') as katalog:
        csvreader = csv.reader(katalog, delimiter=',')
        for row in csvreader:
            tablica.append(row)
    for items in tablica:
        for item in items:
            if item.lower() == tytul.lower():
                tablica.remove(items)
    with open('katalog.csv', 'w', newline='') as katalog:
        csvwriter = csv.writer(katalog, delimiter=',')
        for item in tablica:
            csvwriter.writerow(item)
    print("Udało się usunąć książkę. Lista książek to: ")
    with open('katalog.csv', 'r', newline='') as czytaj:
        csvreader = csv.reader(czytaj, delimiter=',')
        for row in csvreader:
            print(row)

    with open('wypozyczenia.csv', 'r', newline='') as wypozyczenia:
        csvreader = csv.reader(wypozyczenia, delimiter=',')
        for row in csvreader:
            tablica1.append(row)
    for items in tablica1:
        for item in items:
            if item.lower() == tytul.lower():
                tablica1.remove(items)
    with open('wypozyczenia.csv', 'w', newline='') as wypozyczenia:
        csvwriter = csv.writer(wypozyczenia, delimiter=',')
        for item in tablica1:
            csvwriter.writerow(item)

def dodaj_czytelnika():
    with open('loginy.csv', 'a', newline='') as rejestracja:
        csvwriter = csv.writer(rejestracja)
        login = str(input("Podaj login: "))
        haslo = str(input("Podaj haslo: "))
        register = ['-', '-', login, haslo]
        csvwriter.writerow(register)
        print("Udało ci się założyć konto dla czytelnika.")
