import ast
from pprint import pprint


class AC3:

    def __init__(self):
        self.constraints_array = []
        self.constraints_graph = []
        self.variables = []
        self.assigned = []
        self.domains = []

    def addConstraint(self, var1, var2, verifier):
        self.constraints_array.append([var1, var2, verifier])

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
        return self.variables[i] != self.variables[j]

    def eqVerifier(self, i, j):
        return self.variables[i] == self.variables[j]

    def sameDiagonalVerifier(self, i, j):
        return abs(i - j) == abs(self.variables[i] - self.variables[j])

    def notSameDiagonalVerifier(self, i, j):
        return not self.sameDiagonalVerifier(i, j)

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

            else:
                if tab[0] == "allDifferent":
                    for i in range(len(self.variables)):
                        for j in range(i+1, len(self.variables)):
                            self.addConstraint(i, j, self.diffVerifier)


test=AC3()
test.parseProblemFromFile()
test.buildConstraintGraph()

pprint(test.constraints_array)
print(test.constraints_graph)
print(test.domains)
print(test.variables)