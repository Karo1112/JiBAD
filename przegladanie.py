import csv


def przegladaj_katalog():
    print("Wybierz opcję przeglądania katalogu: ")
    print("[1] Po tytule")
    print("[2] Po autorze")
    print("[3] Po słowach kluczowych")
    print("[0] Wyjdź")

    while True:
        opcja = str(input(">> "))
        if opcja == '1':
            tablica = []
            with open('katalog.csv', 'r', newline='') as katalog:
                tytul = str(input("Podaj tytuł książki, która Cię interesuje: "))
                csvreader = csv.reader(katalog, delimiter=',')
                for row in csvreader:
                    tablica.append(row)
            i = 0
            for items in tablica:
                if items[0].lower() == tytul.lower():
                    i += 1
                    print(items)
            if i == 0:
                print("Brak takich książek.")
        elif opcja == '2':
            tablica = []
            with open('katalog.csv', 'r', newline='') as katalog:
                autor = str(input("Podaj imię i nazwisko autora, którego książki Cię interesują: "))
                csvreader = csv.reader(katalog, delimiter=',')
                for row in csvreader:
                    tablica.append(row)
            i = 0
            for items in tablica:
                if items[1].lower() == autor.lower():
                    i += 1
                    print(items)
            if i == 0:
                print("Brak książek tego autora.")
        elif opcja == '3':
            tablica = []
            slowa = []
            with open('katalog.csv', 'r', newline='') as katalog:
                csvreader = csv.reader(katalog, delimiter=',')
                for row in csvreader:
                    tablica.append(row)
                while True:
                    key = str(input("Podaj słowo kluczowe albo wciśnij 0 by zakończyć: "))
                    if key != '0':
                        slowa.append(key)
                    if key == '0':
                        break
            i = 0
            for items in tablica:
                for keys in slowa:
                    if keys.lower() in items[2].lower():
                        print(items)
                        i += 1
            if i == 0:
                print("Brak pasujących książek do powyższych słów kluczowych. ")
        elif opcja == '0':
            break
        else:
            print("Podana opcja nie istnieje, wybierz jeszcze raz.")
