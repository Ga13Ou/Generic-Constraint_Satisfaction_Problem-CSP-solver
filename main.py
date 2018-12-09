from BackTracking import BackTracking
from ForwardChecking import ForwardChecking
import time


def main():
    file_name=input("Choisir le nom du fichier contenant le probleme: (problem.txt est le fichier par defaut) ")
    algo=input("Utiliser BackTracking ou ForwardChecking: [BT/FC]: ")
    heur=input("Activer l'heuristique MRV et DH? [O/N]: ")
    ac3=input("Activer l'utilisation de l'algorithme AC3? [O/N]: ")


    AC3_print="Non"
    heur_print="Non"
    algorithm_print="BackTracking"
    if algo.lower()=="fc":
        solver=ForwardChecking()
        algorithm_print = "ForwardChecking"

    else:
        solver=BackTracking()
    if file_name !="":
        solver.setProblemFileName("testExample/"+file_name)
    solver.parseProblemFromFile()
    if heur.lower()=="o":
        solver.activateHeuristicsMrvDh()
        heur_print="Oui"
    if ac3.lower()=="o":
        solver.activateAC3()
        AC3_print="Oui"
    start_time=time.time()
    solver.initial_log(algorithm_print,AC3_print,heur_print)
    result=solver.solve()
    finish_time=time.time()
    solver.final_log(result,finish_time-start_time)


    print("\n")
    print("Rapport:")
    print("\talgorithm: {}".format(algorithm_print))
    print("\tAC3 active: {}".format(AC3_print))
    print("\tHeuristique MRV et DH active: {}".format(heur_print))
    print("\ttemps d'execution: {} secondes".format(finish_time-start_time))
    print("\tnombre d'iterations: {}".format(solver.get_number_of_iterations()))
    if result:
        print("\tsolution: "+str(solver.variables))
    else:
        print("\tle probleme n'a pas de solution")

main()
