from BackTracking import BackTracking
from ForwardChecking import ForwardChecking
import time


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
    solver.parseProblemFromFile()
    if heur.lower()=="o":
        solver.activateHeuristicsMrvDh()
    if ac3.lower()=="o":
        solver.activateAC3()
    start_time=time.time()
    result=solver.solve()
    finish_time=time.time()
    if result:
        print(solver.variables)
    else:
        print("le probleme n'a pas de solution")
    print("temps d'execution: {} secondes".format(finish_time-start_time))
    print("nombre d'iterations: {}".format(solver.get_number_of_iterations()))

main()
