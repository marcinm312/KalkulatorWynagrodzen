class Pracownik:
    def __init__(self, imie, brutto):
        self.imie = imie
        self.brutto = brutto
        self.skladki = 0.00

    def pobierz_imie(self):
        return self.imie

    def oblicz_wyn_netto(self):
        a = self.brutto
        c = round(round(a * 0.0976, 2) + round(a * 0.015, 2) + round(a * 0.0245, 2), 2)
        d = round(a - c, 2)
        e = round(d * 0.09, 2)
        f = round(d * 0.0775, 2)
        g = 111.25
        h = round(a - g - c, 0)
        i = round(h * 0.18, 2) - 46.33
        j = round(i - f, 0)
        k = round(a - c - e - j, 2)
        return k

    def oblicz_skladki_prac(self):
        a = self.brutto
        skladki = round(round(a * 0.0976, 2) + round(a * 0.065, 2) + round(a * 0.0193, 2) + round(a * 0.0245, 2) + round(a * 0.001, 2), 2)
        self.skladki = skladki
        return skladki

    def oblicz_laczny_koszt(self):
        return self.brutto + self.skladki

wyniki = []
laczny_koszt = 0

print("Podaj liczbę pracowników:")
ile_pracownikow = int(input())
for i in range(ile_pracownikow):
    print("Podaj imię pracownika")
    imie = input()
    print("Podaj wynagrodzenie brutto pracownika")
    brutto = float(input())
    pracownik = Pracownik(imie, brutto)
    netto = '%.2f' % pracownik.oblicz_wyn_netto()
    skladki = '%.2f' % pracownik.oblicz_skladki_prac()
    koszt = '%.2f' % pracownik.oblicz_laczny_koszt()
    wyniki.append(pracownik.pobierz_imie() + "\nWynagrodzenie netto: " + netto + " Składki pracodawcy: " + skladki + " Łączny koszt na pracownika: " + koszt)
    laczny_koszt = laczny_koszt + pracownik.oblicz_laczny_koszt()
for y in range(len(wyniki)):
    print(wyniki[y])
print("\nŁączny koszt dla pracodawcy: " + ('%.2f' % laczny_koszt))