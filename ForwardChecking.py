from copy import deepcopy
from CSP import CSP
from pprint import pprint


class ForwardChecking(CSP):

    def FC(self, varIndex: int, varArray: list, varDomain):
        for i in range(varIndex + 1, len(self.variables)):
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
        if currentIndex == len(self.variables):
            self.variables = varArray
            self.domains = varDomain
            return True
        for value in varDomain[currentIndex]:
            varArray[currentIndex] = value
            self.assigned[currentIndex] = 1
            varArrayCopy = deepcopy(varArray)  # Save
            varDomainCopy = deepcopy(varDomain)
            if self.FC(currentIndex, varArray, varDomain):
                if self.forwardSolver(currentIndex + 1, varArray, varDomain):
                    return True
            self.variables = varArray = varArrayCopy  # restore
            self.domains = varDomain = varDomainCopy
            self.assigned[currentIndex] = 0
        return False

    def solve(self):
        self.parseProblemFromFile()
        print(self.forwardSolver(0, self.variables, self.domains))


# test
a = ForwardChecking()
# a.setProblemFileName("testExample/mapColoringProblem.txt")
a.setProblemFileName("testExample/sudokuProblem.txt")
a.solve()
print(a.variables)
pprint(a.domains)
