patterns = ['aab', 'abc', 'cba']  # wzorce
tekst = 'aaabc'


class AhoCorasick:
    def __init__(self, patterns):
        self.patterns = patterns
        self.trie = []

    def __repr__(self):
        return repr(self.trie)

    def nastepny_stan(self, stan, litera):
        for wezel in self.trie[stan][
            'nastepny_stan']:  # przeszukujemy następny stan obecnego stanu żeby sprawdzić czy litery są takie same
            if self.trie[wezel][
                'litera'] == litera:  # jeśli są to zwracamy ten węzeł, wtedy wiemy że możemy dalej się przesunąć po tej gałęzi
                return wezel
        return None

    def build(self):

        self.trie.append({'litera': '', 'obecny_stan': 0, 'nastepny_stan': [], 'fail_link': 0,
                          'wzorzec': []})  # zaczynamy z tym/ obecny_stan = 0 bo idziemy od "korzenia"
        for x in patterns:  # przeszukujemy po kolei patterny
            stan = 0  # (obecny stan)-zaczynamy od stanu 0 czyli od korzenia
            literka = 0  # przeszukiwanie literek w patternie
            nastepnik = self.nastepny_stan(stan, x[
                literka])  # szukamy nastepnika (od korzenia)w którym litery się powtarzają // dla pierwszego słowa się to nie wykona
            while nastepnik != None:  # najdłuższe wystąpienie który istnieje/przy pierwszym słowie się to nie wykona
                stan = nastepnik
                literka += 1
                if literka < len(x):  # nie możemy wyjść poza długość słowa, mniejsze niż długość bo zaczynamy od 0
                    nastepnik = self.nastepny_stan(stan, x[literka])
                else:
                    break
            for i in range(literka,
                           len(x)):  # przeszukujemy reszte wzorca, którego jeszcze nie ma, czyli zaczyny od tego miejsca słowa, które się jeszcze nie powtarza
                self.trie[stan]['nastepny_stan'].append(
                    len(self.trie))  # najpierw dodamy następny stan dla obecnego stanu i to będzie długość obecnego drzewa
                self.trie.append({'litera': x[i], 'obecny stan': len(self.trie), 'nastepny_stan': [], 'fail_link': 0,
                                  'wzorzec': []})  # tworzymy takie zbiory, litera to obecna literka, stan to obecna długość drzewa ponieważ ciągle dodajemy węzły
                stan = len(self.trie) - 1  # stan to dlugość drzewa odjąć jeden bo zaczynamy od 0
            self.trie[stan]['wzorzec'].append(x)  # jak dodamy cały wzorzec to możemy go sobie wypisać
        print(self.trie)  # tu sprawdzam czy się wszystko zgadza bez faillinków
        self.fail_linki()
        print(self.trie)  # tu sprawdzam czy się wszystko zgadza z faillinkami

    def fail_linki(self):
        kolejka = []  # tu będziemy zapisywać i usuwać węzły z przeszukiwania wszerz (BFS)
        nastepnik = 0
        for wezel in self.trie[0][
            'nastepny_stan']:  # szukamy krawędzi od korzenia (następny stan) i ustawiamy tam fail-linki do niego czyli równe 0
            kolejka.append(wezel)  # każdy taki węzeł wrzucamy do kolejki
            self.trie[wezel]['fail_link'] = 0
        while kolejka:
            remove = kolejka.pop(0)  # to co usuwamy z kolejki po lewej strony bo mamy przeszukiwanie wszerz
            for nastepnik in self.trie[remove]['nastepny_stan']:  # szukamy następników tego usuniętego węzła
                kolejka.append(nastepnik)  # dodajemy ten następny stan do kolejki
                stan = self.trie[remove][
                    'fail_link']  # odczytujemy faillinki tych wcześniejszych stanów, żeby wiedzieć jak wrócić po drzewie

                self.trie[nastepnik]['fail_link'] = self.nastepny_stan(stan, self.trie[nastepnik][
                    'litera'])  # idziemy po faillinku przodka i sprawdzamy czy możemy zmienić gałąź
                if self.trie[nastepnik][
                    'fail_link'] is None:  # jeśli nie ma takiego failinka to znaczy że musimy wrócić do korzenia
                    self.trie[nastepnik]['fail_link'] = 0

    def search(self, tekst):
        stan = 0
        znalezione = []
        for i in range(0, len(tekst)):  # przeszukujemy cały tekst
            while self.nastepny_stan(stan, tekst[
                i]) is None and stan != 0:  # jeśli stan się nie zgadza to musimy wrócić po fail_linku
                stan = self.trie[stan]['fail_link']
            stan = self.nastepny_stan(stan, tekst[i])  # jeśli jest dopasowanie wzorca to idziemy po tych gałęziach
            if stan is None:
                stan = 0
            else:
                for j in self.trie[stan]['wzorzec']:  # będzie wywołane jak znajdziemy wzorzec
                    znalezione.append({'indeks': i - len(j) + 1, 'wzorzec': j})
        print(znalezione)


ahocorasick = AhoCorasick(['aab', 'abc', 'cba'])
ahocorasick.build()
ahocorasick.search('aaabc')
print(repr(ahocorasick))
