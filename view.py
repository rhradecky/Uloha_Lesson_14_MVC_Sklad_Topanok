from controller import Sklad

class Skladove_zasoby(Sklad):
    def zobraz_skladove_zasoby(self):
        dostupne_topanky = [topanky for topanky in self.na_sklade]
        if dostupne_topanky:
            print("Dostupne skladove zasoby:")
            for topanky in dostupne_topanky:
                print(topanky.znacka)
        else:
            print("Ziadne topanky nie su dostupne.")

