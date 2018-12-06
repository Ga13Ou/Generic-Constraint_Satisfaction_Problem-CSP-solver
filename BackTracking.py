from CSP import CSP
from copy import deepcopy


class BackTracking(CSP):

    def BT(self, index: int):
        # used to not break the code when activating the heuristique cause whith my algorithm when
        # heuristics are activated we need to always get the first element of the array
        if self.heuristic_is_activated:
            heurIndex=0
        else:
            heurIndex=index
        ######
        if index == len(self.variables):
            return True
        self.updateHeuristics()
        for k in range(len(self.domains[self.heur_array[heurIndex]])):
            self.variables[self.heur_array[heurIndex]] = self.domains[self.heur_array[heurIndex]][k]
            self.assigned[self.heur_array[heurIndex]] = 1
            heur_array_copy=deepcopy(self.heur_array) #Save
            if (self.checkAllConstraints()):
                if (self.BT(index + 1)):
                    return True
            self.assigned[self.heur_array[heurIndex]] = 0
            self.heur_array=heur_array_copy #Restore
        return False

    def solve(self):
        print("tessst")
        self.BT(0)


# test
a = BackTracking()
# a.setProblemFileName("testExample/mapColoringProblem.txt")
a.setProblemFileName("testExample/sudokuProblem.txt")
a.parseProblemFromFile()

a.activateHeuristicsMrvDh()
a.solve()
print(a.variables)

expected="397286541412539768856471329284195637639748215571362894728913456163854972945627183"
actual="".join(str(x) for x in a.variables)
print(expected==actual)
# print(a.variables)
