import csv
import opcje_bibliotekarza
import przegladanie
import opcje_czytelnika

bibliotekarz = False
czytelnik = False

print("LOGOWANIE\nWybierz jako kto chcesz się zalogować: ")
print("[1] Bibliotekarz")
print("[2] Czytelnik")
print("[0] Wyjdź")


while True:
    logowanie = str(input(">> "))
    if logowanie == '1':
        opcja = str(input("Jeżeli chcesz założyć nowe konto wciśnij 1, jeżeli chcesz się zalogować wciśnij 0. "))
        if opcja == '0':
            with open('loginy.csv', 'r', newline='') as loginy:
                reader = csv.reader(loginy, delimiter=',')
                login = str(input("Podaj login: "))
                for row in reader:
                    if login in row:
                        password = str(input("Podaj hasło: "))
                        if password == row[1]:
                            print("Udało ci się zalogować na konto bibliotekarza.")
                            bibliotekarz = True
                            break
                        else:
                            print("Błędne hasło, zaloguj się jeszcze raz.")
                break
        elif opcja == '1':
            with open('loginy.csv', 'a', newline='') as rejestracja:
                csvwriter = csv.writer(rejestracja)
                login = str(input("Podaj login"))
                haslo = str(input("Podaj haslo"))
                register = [login, haslo, '-', '-']
                csvwriter.writerow(register)
                print("Udało ci się założyć konto i zalogować.")
                bibliotekarz = True
                break
        else:
            print("Podana opcja nie istnieje, wybierz jeszcze raz, jako kto chcesz się zalogować.")
    elif logowanie == '2':
        with open('loginy.csv', 'r', newline='') as loginy:
            reader = csv.reader(loginy, delimiter=',')
            login = str(input("Podaj login: "))
            for row in reader:
                if login in row:
                    password = input("Podaj hasło: ")
                    if password == row[3]:
                        print("Udało ci się zalogować na konto czytelnika.")
                        czytelnik = True
                        break
                    else:
                        print("Błędne hasło, zaloguj się jeszcze raz.")
            break
    elif logowanie == '0':
        break
    else:
        print("Taka opcja nie istnieje, wybierz jeszcze raz.")

if bibliotekarz:
    print("Dostępne opcje to: ")
    print("[1] Zwrot książki")
    print("[2] Dodaj nową książkę")
    print("[3] Usuń książkę z systemu")
    print("[4] Dodaj czytelnika")
    print("[5] Przeglądaj katalog")
    print("[0] Wyjdź")

    while True:
        opcja = str(input(">> "))
        if opcja == '1':
            opcje_bibliotekarza.zwrot_ksiazki()
            break
        elif opcja == '2':
            opcje_bibliotekarza.dodaj_ksiazke()
            break
        elif opcja == '3':
            opcje_bibliotekarza.usun_ksiazke()
            break
        elif opcja == '4':
            opcje_bibliotekarza.dodaj_czytelnika()
            break
        elif opcja == '5':
            przegladanie.przegladaj_katalog()
            break
        elif opcja == '0':
            print("Zakończyłeś działanie")
            break
        else:
            print("Nie ma takiej opcji, wybierz jeszcze raz.")


if czytelnik:
    print("Dostępne opcje to: ")
    print("[1] Wypożycz książkę")
    print("[2] Zarezerwuj książkę")
    print("[3] Przedłuż wypożyczenie")
    print("[4] Przeglądaj katalog")
    print("[0] Wyjdź")

    while True:
        opcja = str(input(">> "))
        if opcja == '1':
            opcje_czytelnika.wypozycz_ksiazke(login)
            break
        elif opcja == '2':
            opcje_czytelnika.zarezerwuj_ksiazke(login)
            break
        elif opcja == '3':
            opcje_czytelnika.przedluz_wypozyczenie(login)
            break
        elif opcja == '4':
            przegladanie.przegladaj_katalog()
            break
        elif opcja == '0':
            print("Zakończyłeś działanie")
            break
        else:
            print("Nie ma takiej opcji, wybierz jeszcze raz: ")
