from BackTracking import BackTracking
from ForwardChecking import ForwardChecking

def main():
    pass

def menu_1():
    print("=====================Menu======================")
    print("=1- choisir le fichier contenant le probleme  =")
    print("=2- choisir l'algorithme de BackTracking"
          "  1- AC3 "
          "  2- AC3 && MRV      =")
    print("=3- choisir l'algorithme de ForwardChecking   =")
    print("===============================================")

    a=int(input("votre choix: "))
    if a < 1 or a>3:
        return menu_1()
    return a

def menu_2():
    print("=====================Menu=======================")
    print("=1- Activer l'heuristique MRV et DH            =")
    print("=2- Activer l'AC3                              =")
    print("=3- Activer l'AC3 et l'heuristique MRV et DH   =")
    print("=0- Ne rien activer                            =")
    print("================================================")
    a = int(input("votre choix: "))
    if a < 0 or a > 3:
        return menu_2()
    return a
menu_1()
