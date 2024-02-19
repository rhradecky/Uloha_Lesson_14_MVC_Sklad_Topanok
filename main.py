from controller import Sklad
from model import Topanky
from view import Skladove_zasoby

topanka1 = Topanky("Male", "Sneakers", "White", 50, "Nike", 12, 1020)
topanka2 = Topanky("Male", "Sneakers", "Black", 50, "Adidas", 10, 1021)
topanka3 = Topanky("Male", "Sneakers", "White/Green", 100, "Nike", 10, 1022)
topanka4 = Topanky("Male", "Sneakers", "White", 50, "Nike", 7, 1023)
topanka5 = Topanky("Male", "Sneakers", "Black", 50, "Adidas", 3, 1024)
topanka6 = Topanky("Male", "Sneakers", "White/Green", 33, "Nike", 8, 1025)
topanka7 = Topanky("Male", "Sneakers", "White/Green", 22, "Nike", 9, 1026)
topanka8 = Topanky("Male", "Sneakers", "White", 66, "Nike", 9, 1027)
topanka9 = Topanky("Male", "Sneakers", "Black", 77, "Adidas", 15, 1028)
topanka10 = Topanky("Male", "Sneakers", "White/Green", 99, "Nike", 8, 1029)

sklad = Sklad()
skladove_zasoby = Skladove_zasoby()

sklad.pridaj_topanky(topanka1); sklad.pridaj_topanky(topanka2); sklad.pridaj_topanky(topanka3); sklad.pridaj_topanky(topanka4); sklad.pridaj_topanky(topanka5)
sklad.pridaj_topanky(topanka6); sklad.pridaj_topanky(topanka7); sklad.pridaj_topanky(topanka8); sklad.pridaj_topanky(topanka9); sklad.pridaj_topanky(topanka10)
print("------------------------------------------------------------------------------------------------- ")
sklad.zobraz_skladove_zasoby()

sklad.odstran_topanky(1022); sklad.odstran_topanky(1025); sklad.odstran_topanky(1028)
print("------------------------------------------------------------------------------------------------- ")
sklad.zobraz_skladove_zasoby()
print("------------------------------------------------------------------------------------------------- ")
sklad.topanky_podla_velkosti(9)

sklad.celkova_cena_skladu()
