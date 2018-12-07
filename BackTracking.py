from CSP import CSP
from AC3 import AC3
from copy import deepcopy


class BackTracking(AC3):

    def BT(self, index: int):
        if index == len(self.variables):
            return True
        heurIndex = self.convert_index(index)
        self.updateHeuristics()
        for k in range(len(self.domains[self.heur_array[heurIndex]])):
            self.variables[self.heur_array[heurIndex]] = self.domains[self.heur_array[heurIndex]][k]
            self.assigned[self.heur_array[heurIndex]] = 1 #Save
            heur_array_copy=deepcopy(self.heur_array)
            currentVarDomainCopy = deepcopy(self.domains[self.heur_array[heurIndex]])
            self.domains[self.heur_array[heurIndex]] = [self.variables[self.heur_array[heurIndex]]]
            domainsCopy=deepcopy(self.domains)
            if (self.checkAllConstraints()):
                if self.AC3_is_activated:
                    # print("allo")
                    self.arcConsistency3(heurIndex)
                    # print("am here")
                if (self.BT(index + 1)):
                    return True
            self.assigned[self.heur_array[heurIndex]] = 0 #Restore
            self.heur_array=heur_array_copy
            self.domains=domainsCopy
            self.domains[self.heur_array[heurIndex]] = currentVarDomainCopy
        return False

    def solve(self):
        if self.AC3_is_activated:
            self.initArcConsistency3()
            print("Arc Consistency Done")
        return self.BT(0)


# # test
# a = BackTracking()
# # a.setProblemFileName("testExample/mapColoringProblem.txt")
# # a.setProblemFileName("testExample/sudokuProblem.txt")
# a.parseProblemFromFile()
# a.activatedAC3()
# #a.activateHeuristicsMrvDh()
# a.solve()
# print(a.variables)
#
# expected="397286541412539768856471329284195637639748215571362894728913456163854972945627183"
# actual="".join(str(x) for x in a.variables)
# print(expected==actual)
# # print(a.variables)
