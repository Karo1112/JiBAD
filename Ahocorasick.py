patterns = ['aab', 'abc', 'cba'] #wzorce
tekst = 'aaabc'

trie = []
def nastepny_stan(stan, litera):
    for wezel in trie[stan]['nastepny_stan']: #przeszukujemy następny stan obecnego stanu żeby sprawdzić czy litery są takie same
        if trie[wezel]['litera'] == litera:  #jeśli są to zwracamy ten węzeł, wtedy wiemy że możemy dalej się przesunąć po tej gałęzi
            return wezel
    return None

def build(patterns):
    trie.append({'litera': '', 'obecny_stan': 0,'nastepny_stan': [], 'fail_link': 0, 'wzorzec': []}) #zaczynamy z tym/ obecny_stan = 0 bo idziemy od "korzenia"
    for x in patterns: #przeszukujemy po kolei patterny
        stan = 0 #(obecny stan)-zaczynamy od stanu 0 czyli od korzenia
        literka = 0 #przeszukiwanie literek w patternie
        nastepnik = nastepny_stan(stan, x[literka]) #szukamy nastepnika (od korzenia)w którym litery się powtarzają // dla pierwszego słowa się to nie wykona
        while nastepnik != None: #najdłuższe wystąpienie który istnieje/przy pierwszym słowie się to nie wykona
            stan = nastepnik
            literka += 1
            if literka < len(x): #nie możemy wyjść poza długość słowa, mniejsze niż długość bo zaczynamy od 0
                nastepnik = nastepny_stan(stan, x[literka])
            else:
                break
        for i in range(literka, len(x)): #przeszukujemy reszte wzorca, którego jeszcze nie ma, czyli zaczyny od tego miejsca słowa, które się jeszcze nie powtarza
            trie[stan]['nastepny_stan'].append(len(trie)) #najpierw dodamy następny stan dla obecnego stanu i to będzie długość obecnego drzewa
            trie.append({'litera': x[i],'obecny stan': len(trie), 'nastepny_stan': [], 'fail_link': 0, 'wzorzec': []})#tworzymy takie zbiory, litera to obecna literka, stan to obecna długość drzewa ponieważ ciągle dodajemy węzły
            stan = len(trie) -1 #stan to dlugość drzewa odjąć jeden bo zaczynamy od 0
        trie[stan]['wzorzec'].append(x) #jak dodamy cały wzorzec to możemy go sobie wypisać
    print(trie) #tu sprawdzam czy się wszystko zgadza bez faillinków
    fail_linki()
    print(trie) #tu sprawdzam czy się wszystko zgadza z faillinkami

def fail_linki():
    kolejka = [] #tu będziemy zapisywać i usuwać węzły z przeszukiwania wszerz (BFS)
    nastepnik = 0
    for wezel in trie[0]['nastepny_stan']: #szukamy krawędzi od korzenia (następny stan) i ustawiamy tam fail-linki do niego czyli równe 0
        kolejka.append(wezel) #każdy taki węzeł wrzucamy do kolejki
        trie[wezel]['fail_link'] = 0
    while kolejka:
        remove = kolejka.pop(0)#to co usuwamy z kolejki po lewej strony bo mamy przeszukiwanie wszerz
        for nastepnik in trie[remove]['nastepny_stan']: #szukamy następników tego usuniętego węzła
            kolejka.append(nastepnik) #dodajemy ten następny stan do kolejki
            stan = trie[remove]['fail_link'] #odczytujemy faillinki tych wcześniejszych stanów, żeby wiedzieć jak wrócić po drzewie

            trie[nastepnik]['fail_link'] = nastepny_stan(stan, trie[nastepnik]['litera']) #idziemy po faillinku przodka i sprawdzamy czy możemy zmienić gałąź
            if trie[nastepnik]['fail_link'] is None: #jeśli nie ma takiego failinka to znaczy że musimy wrócić do korzenia
                trie[nastepnik]['fail_link'] = 0

def search(tekst):
    stan = 0
    znalezione = []
    for i in range(0,len(tekst)): #przeszukujemy cały tekst
        while nastepny_stan(stan, tekst[i]) is None and stan != 0: #jeśli stan się nie zgadza to musimy wrócić po fail_linku
            stan = trie[stan]['fail_link']
        stan = nastepny_stan(stan, tekst[i]) #jeśli jest dopasowanie wzorca to idziemy po tych gałęziach
        if stan is None:
            stan = 0
        else:
            for j in trie[stan]['wzorzec']: #będzie wywołane jak znajdziemy wzorzec
                znalezione.append({'indeks': i-len(j) + 1, 'wzorzec': j})
    print(znalezione)


build(patterns)
search(tekst)





