import ast
from pprint import pprint

class CSP:
    def __init__(self):
        self.constraints_array = []
        self.constants_constraints_array = []  # this is for the constraints between a variable and a constant example: var2=5
        self.constraints_graph = []
        self.variables = []
        self.assigned = []
        self.domains = []

    def addConstraint(self, var1, var2, verifier):
        self.constraints_array.append([var1, var2, verifier])

    def addConstantConstraint(self, varIndex, constant, verifier):
        self.constants_constraints_array.append([varIndex, constant, verifier])

    def buildConstraintGraph(self):
        # you have to set Variables number and add all constraints before using this method
        for constraint in self.constraints_array:
            if constraint[0] not in self.constraints_graph[constraint[1]]:
                self.constraints_graph[constraint[1]].append(constraint[0])
            if constraint[1] not in self.constraints_graph[constraint[0]]:
                self.constraints_graph[constraint[0]].append(constraint[1])

    def setVariablesNumber(self, N):
        self.variables = [-1 for i in range(N)]
        self.assigned = [0 for i in range(N)]
        self.constraints_graph = [[] for i in range(N)]

    def diffVerifier(self, i, j):
        if self.assigned[i] * self.assigned[j] == 0:
            return True
        return self.variables[i] != self.variables[j]

    def eqVerifier(self, i, j):
        if self.assigned[i] * self.assigned[j] == 0:
            return True
        return self.variables[i] == self.variables[j]

    def sameDiagonalVerifier(self, i, j):
        if self.assigned[i] * self.assigned[j] == 0:
            return True
        return abs(i - j) == abs(self.variables[i] - self.variables[j])

    def notSameDiagonalVerifier(self, i, j):
        if self.assigned[i] * self.assigned[j] == 0:
            return True
        return not self.sameDiagonalVerifier(i, j)

    def constEqVerifier(self, i, a):
        if self.assigned[i] == 0:
            return True
        return self.variables[i] == a

    def constDiffVerifier(self, i, a):
        if self.assigned[i] == 0:
            return True
        return self.variables[i] != a

    def setDomains(self, array):
        self.domains = array

    def parseProblemFromFile(self):
        problem = open("problem.txt", "r")
        fileContent = []
        for line in problem.readlines():
            if line[0] != "#":
                fileContent.append(line.replace("\n", ""))
        n = int(fileContent[0])
        self.setVariablesNumber(n)
        fileContent = fileContent[1:]
        domain = []
        for i in range(n):
            tab = ast.literal_eval(fileContent[i])
            domain.append(tab)
        self.setDomains(domain)
        fileContent = fileContent[n:]
        self.parseConstraints(fileContent)

    def parseConstraints(self, array):
        for line in array:
            tab = line.split(";")
            if len(tab) == 3:
                if tab[0] == "diff":
                    self.addConstraint(int(tab[1]), int(tab[2]), self.diffVerifier)
                elif tab[0] == "eq":
                    self.addConstraint(int(tab[1]), int(tab[2]), self.eqVerifier)
                elif tab[0] == "notSameDiagonal":
                    self.addConstraint(int(tab[1]), int(tab[2]), self.notSameDiagonalVerifier)
                elif tab[0] == "constEq":
                    self.addConstantConstraint(tab[1], tab[2], self.constEqVerifier)
                elif tab[0] == "constDiff":
                    self.addConstantConstraint(tab[1], tab[2], self.constDiffVerifier)

            else:
                if tab[0] == "allDifferent":
                    for i in range(len(self.variables)):
                        for j in range(i + 1, len(self.variables)):
                            self.addConstraint(i, j, self.diffVerifier)

                if tab[0] == "allNotSameDiag":
                    for i in range(len(self.variables)):
                        for j in range(i + 1, len(self.variables)):
                            self.addConstraint(i, j, self.notSameDiagonalVerifier)

    def checkConstraint(self, constraint):
        return constraint[2](constraint[0], constraint[1])

    def checkAllConstantConstraints(self):
        for constraint in self.constants_constraints_array:
            if not self.checkAllConstraints(constraint):
                return False
        return True

    def checkAllVarConstraints(self):
        for contraint in self.constraints_array:
            if not self.checkConstraint(contraint):
                return False
        return True

    def checkAllConstraints(self):
        return self.checkAllConstantConstraints() and self.checkAllVarConstraints()