from copy import deepcopy
from CSP import CSP
from AC3 import AC3
from pprint import pprint


class ForwardChecking(AC3):

    def FC(self, varIndex: int, varArray: list, varDomain):
        for i in range(len(self.variables)):
            if not self.assigned[i]:
                k = 0
                while k < len(varDomain[i]):
                    varArray[i] = varDomain[i][k]
                    self.assigned[i] = 1
                    if not self.checkAllConstraints():
                        varDomain[i].pop(k)
                        k -= 1
                    k += 1
                    self.assigned[i] = 0
                if (len(varDomain[i]) == 0):
                    # this is when the domain gets empty after FC
                    return False
        return True

    def forwardSolver(self, currentIndex, varArray, varDomain):
        ac_result=True #this line used in case of the ac3 is not activated so we can pass the test of the recursive call
        if currentIndex == len(self.variables):
            self.variables = varArray
            self.domains = varDomain
            return True
        heurIndex=self.convert_index(currentIndex)
        self.updateHeuristics()

        for value in varDomain[self.heur_array[heurIndex]]:
            self.number_of_iterations += 1
            varArray[self.heur_array[heurIndex]] = value
            self.assigned[self.heur_array[heurIndex]] = 1
            varArrayCopy = deepcopy(varArray)  # Save
            varDomainCopy = deepcopy(varDomain)
            heur_array_copy=deepcopy(self.heur_array)
            currentVarDomainCopy=deepcopy(self.domains[self.heur_array[heurIndex]])
            self.domains[self.heur_array[heurIndex]]=[self.variables[self.heur_array[heurIndex]]]
            if self.FC(currentIndex, varArray, varDomain):
                if self.AC3_is_activated:
                    ac_result=self.arcConsistency3(heurIndex)
                    self.log_state(currentIndex, self.heur_array[heurIndex])
                else:
                    self.log_state(currentIndex, self.heur_array[heurIndex])
                if ac_result:
                    if self.forwardSolver(currentIndex + 1, varArray, varDomain):
                        return True
            else:
                self.log_state(currentIndex, self.heur_array[heurIndex])

            self.variables = varArray = varArrayCopy  # restore
            self.domains = varDomain = varDomainCopy
            self.heur_array=heur_array_copy
            self.domains[self.heur_array[heurIndex]]=currentVarDomainCopy
            self.assigned[self.heur_array[heurIndex]] = 0
        return False

    def solve(self):
        if self.AC3_is_activated:
            self.initArcConsistency3()
            print("initialisation de l'arc consistance avec succes")
        return self.forwardSolver(0, self.variables, self.domains)


# test
# a = ForwardChecking()
# # a.setProblemFileName("testExample/mapColoringProblem.txt")
# a.setProblemFileName("testExample/sudokuProblem.txt")
# a.parseProblemFromFile()
# a.activateHeuristicsMrvDh()
# a.activatedAC3()
# a.solve()
# print(a.variables)
# expected="397286541412539768856471329284195637639748215571362894728913456163854972945627183"
# actual="".join(str(x) for x in a.variables)
# print(expected==actual)

