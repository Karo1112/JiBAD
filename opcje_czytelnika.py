import csv
import datetime
dzis=datetime.date.today()
dl=datetime.timedelta(days=7) #niech odpowiada za przedluzenie ksiazki o tydzien
przedluz_ksiazke = dzis+dl


def wypozycz_ksiazke(login):
    tablica = []
    with open('wypozyczenia.csv', 'r', newline='') as wypozycz:
        tytul = str(input("Podaj tytuł książki, którą chcesz wypożyczyć: "))
        csvreader = csv.reader(wypozycz, delimiter=',')
        for row in csvreader:
            tablica.append(row)

    for items in tablica:
        for item in items:
            if tytul.lower() in item.lower():
                if items[2] != 'NIE':
                    print("Podana książka jest już wypożyczona.")
                else:
                    items[2] = str(dzis)
                    items[1] = login
                    with open('wypozyczenia.csv', 'w', newline='') as wypozycz:
                        csvwriter = csv.writer(wypozycz, delimiter=',')
                        for item in tablica:
                            csvwriter.writerow(item)
                        print("Udało ci się wypożyczyć książkę.")


def zarezerwuj_ksiazke(login):
    tablica = []
    with open('wypozyczenia.csv', 'r', newline='') as wypozycz:
        tytul = str(input("Podaj tytuł książki, którą chcesz zarezerwować: "))
        csvreader = csv.reader(wypozycz, delimiter=',')
        for row in csvreader:
            tablica.append(row)

    for items in tablica:
        for item in items:
            if tytul.lower() in item.lower():
                if items[3] != 'NIE':
                    print("Podana książka jest już zarezerwowana.")
                else:
                    items[3] = login
                    with open('wypozyczenia.csv', 'w', newline='') as wypozycz:
                        csvwriter = csv.writer(wypozycz, delimiter=',')
                        for item in tablica:
                            csvwriter.writerow(item)
                        print("Udało Ci się zarezerwować książkę.")

def przedluz_wypozyczenie(login):
    tablica = []
    with open('wypozyczenia.csv', 'r', newline='') as przedluz:
        tytul = str(input("Podaj tytuł książki, którą chcesz przedłużyć: "))
        csvreader = csv.reader(przedluz, delimiter=',')
        for row in csvreader:
            tablica.append(row)

    for items in tablica:
        for item in items:
            if items[0].lower() == tytul.lower():
                if items[1] == login:
                    items[4] = str(przedluz_ksiazke)
                else:
                    print("Podana książka nie jest przez Ciebie wypożyczona, nie możesz jej przedłużyć")
    with open('wypozyczenia.csv', 'w', newline='') as wypozycz:
        csvwriter = csv.writer(wypozycz, delimiter=',')
        for item in tablica:
            csvwriter.writerow(item)
        print("Udało ci się przedłużyć książkę o tydzień.")