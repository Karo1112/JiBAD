import csv

print("------------Katalog--------------\n")
with open('katalog.csv', 'r', newline='') as czytaj:
    csvreader = csv.reader(czytaj, delimiter=',')
    for row in csvreader:
        print(row)

print("\n--------------Loginy------------------\n")
with open('loginy.csv', 'r', newline='') as czytaj:
    csvreader = csv.reader(czytaj, delimiter=',')
    for row in csvreader:
        print(row)


print("\n--------------Wypożyczenia--------------\n")
with open('wypozyczenia.csv', 'r', newline='') as czytaj:
    csvreader = csv.reader(czytaj, delimiter=',')
    for row in csvreader:
        print(row)