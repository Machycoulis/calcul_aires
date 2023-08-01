from math import pi
import time, sys

FORMES = ("c - carré", "r - rectangle", "t - triangle", "cc - cercle")
FORMES_CHOIX = ("c", "re", "t", "cc")

#______def des fonctions par forme
def carre_aire():
        car_aire = int(car_l**2)
        print(f"Aire du carré: {car_aire} cm2")

def rect_aire():
    rect_aire = int(rect_l*rect_h)
    print(f"Aire du rectangle: {rect_aire} cm2")

def tri_aire():
    tri_aire = int((tri_h*tri_l)/2)
    print(f"Aire du triangle: {tri_aire} cm2")

def cc_aire():
    cc_aire = int(pi * cc_r**2)
    print(f"Aire du cercle: {cc_aire} cm2")

#______fonction cool trouvée sur un site en faisant des recherches sur time.sleep

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

#_______ici je demande de quelle forme calculer l'aire

typingPrint("Bonjour, nous sommes ici pour calculer l'aire de tes murs.\n")
time.sleep(1)

typingPrint("Quelle est la forme de ton mur?\n")
time.sleep(1)

for i in FORMES[0:4]:
    print(i)
    time.sleep(1)

forme = input("Forme: ").lower()

#______calculs selon les entrées

while forme not in FORMES_CHOIX:
   typingPrint("Entrée incorrecte. Veuillez choisir entre c|r|t|cc \n")
   forme = input("Forme :").lower()
else:
   if forme == "c":
      car_l = float(input("Longueur (cm) ="))
      carre_aire()

   if forme == "r":
       rect_l = float(input("Longueur (cm) ="))
       rect_h = float(input("Hauteur (cm) ="))
       rect_aire()
   if forme == "t":
       tri_l = float(input("Longueur (cm) ="))
       tri_h = float(input("Hauteur (cm) ="))
       tri_aire()
   if forme == "cc":
       cc_r = float(input("Rayon (cm) ="))
       cc_aire()

