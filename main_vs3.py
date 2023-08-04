from math import pi
import time, sys

FORMES = ("c - carré", "r - rectangle", "t - triangle", "cc - cercle")
FORMES_CHOIX = ("c", "r", "t", "cc")

#______def des fonctions par forme
def carre_aire():
    aire = float((car_l**2)*0.0001)
    print(f"Aire du carré: {aire} m2")
    return aire

def rectangle_aire():
    aire = float((rect_l*rect_h)*0.0001)
    print(f"Aire du rectangle: {aire} m2")
    return aire

def triangle_aire():
    aire = float(((tri_h*tri_l)/2)*0.0001)
    print(f"Aire du triangle: {aire} m2")
    return aire

def cercle_aire():
    aire = float((pi * cc_r**2)*0.0001)
    print(f"Aire du cercle: {aire} m2")
    return aire

def rendement():
    if forme == "c":
        vol_peint = float(carre_aire()/rdm)
        print(f"Il vous faudra {vol_peint} litres de peinture pour XX m2")

    if forme == "r":
        vol_peint = float(rectangle_aire()/rdm)
        print(f"Il vous faudra {vol_peint} litres de peinture pour XX m2")

    if forme == "t":
        vol_peint = float(triangle_aire()/rdm)
        print(f"Il vous faudra {vol_peint} litres de peinture pour XX m2")

    if forme == "cc":
        vol_peint = float(cercle_aire()/rdm)
        print(f"Il vous faudra {vol_peint} litres de peinture pour XX m2")



#______fonction cool trouvée sur un site en faisant des recherches sur time.sleep

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0)

#_______ici je demande de quelle forme calculer l'aire

typingPrint("Bonjour, nous sommes ici pour calculer l'aire de ton support et t'indiquer quelle quantité de peinture sera nécessaire.\n")
time.sleep(0)

typingPrint("Quelle est la forme de ton support?\n")
time.sleep(0)

for i in FORMES[0:4]:
    print(i)
    time.sleep(0)

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
       rectangle_aire()

   if forme == "t":
       tri_l = float(input("Longueur (cm) ="))
       tri_h = float(input("Hauteur (cm) ="))
       triangle_aire()

   if forme == "cc":
       cc_r = float(input("Rayon (cm) ="))
       cercle_aire()

#_____demander rendement de la peinture
typingPrint("Maintenant, quel est le rendement de ta peinture? (m2/L)\n")

while True:
    try:
        rdm = float(input())
    except ValueError:
        print("Entrée invalide. Veuillez indiquer un chiffre.")
    else:
        break

rendement()

