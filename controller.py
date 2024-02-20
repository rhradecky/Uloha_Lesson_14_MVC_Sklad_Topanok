class Sklad:
    def __init__(self):
        self.na_sklade = []

    def pridaj_topanky(self, topanky):
        self.na_sklade.append(topanky)
        print("topanky ", topanky.znacka, "boli pridane do skladu.")

    def zobraz_skladove_zasoby(self):
        dostupne_topanky = [topanky for topanky in self.na_sklade]
        if dostupne_topanky:
            print("Dostupne skladove zasoby:")
            for topanky in dostupne_topanky:
                print("ID: ", topanky.id, "  ", topanky.pohlavie, "  Typ: ", topanky.typ, "   Cena: ", topanky.cena, "   Velkost: ", topanky.velkost,"   ", topanky.znacka, "   Farba: ", topanky.farba, )
        else:
            print("Ziadne topanky nie su na sklade.")


    def odstran_topanky(self, id):
        for topanky in self.na_sklade:
            if topanky.id == id:
                self.na_sklade.remove(topanky)
                print("topanky s ID:", topanky.id, "boli odstranene.")

    def topanky_podla_velkosti(self, velkost):
        for topanky in self.na_sklade:
            if topanky.velkost == velkost:
                print("ID: ", topanky.id, "  ", topanky.pohlavie, "  Typ: ", topanky.typ, "   Cena: ", topanky.cena, "   Velkost: ", topanky.velkost,"   ", topanky.znacka, "   Farba: ", topanky.farba, )

    def celkova_cena_skladu(self):
        celkova_cena = 0
        for topanky in self.na_sklade:
            celkova_cena += int(topanky.cena)
        print("Celkova cena skladu:", celkova_cena, "EUR")



