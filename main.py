from BackTracking import BackTracking
from ForwardChecking import ForwardChecking

def main():
    file_name=input("Choisir le nom du fichier contenant le probleme: (problem.txt est le fichier par defaut) ")
    algo=input("Utiliser BackTracking ou ForwardChecking: [BT/FC]: ")
    heur=input("Activer l'heuristique MRV et DH? [O/N]: ")
    ac3=input("Activer l'utilisation de l'algorithme AC3? [O/N]: ")

    if algo.lower()=="fc":
        solver=ForwardChecking()
    else:
        solver=BackTracking()
    if file_name !="":
        solver.setProblemFileName("testExample/"+file_name)
    if heur.lower()=="o":
        solver.activateHeuristicsMrvDh()
    if ac3.lower()=="o":
        solver.activatedAC3()
    solver.parseProblemFromFile()
    result=solver.solve()
    if result:
        print(solver.variables)
    else:
        print("le probleme n'a pas de solution")


main()