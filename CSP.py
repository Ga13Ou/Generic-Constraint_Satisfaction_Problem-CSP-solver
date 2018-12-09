import ast
from functools import cmp_to_key
from pprint import pprint


class CSP:
    def __init__(self):
        self.constraints_array = []
        self.constants_constraints_array = []  # this is for the constraints between a variable and a constant example: var2=5
        self.constraints_graph = []
        self.variables = []
        self.assigned = []
        self.domains = []
        self.problem_file_name = "testExample/Problem.txt"
        self.heur_array = []
        self.constraint_graph_is_built=False
        self.heuristic_is_activated=False
        self.AC3_is_activated=False
        self.number_of_iterations=0
        self.log_file=open("log.txt","w+")

    def addConstraint(self, var1, var2, verifier):
        self.constraints_array.append([var1, var2, verifier])

    def addConstantConstraint(self, varIndex, constant, verifier):
        self.constants_constraints_array.append([varIndex, constant, verifier])

    def buildConstraintGraph(self):
        # you have to set Variables number and add all constraints before using this method
        self.constraint_graph_is_built=True
        for constraint in self.constraints_array:
            if constraint[0] not in self.constraints_graph[constraint[1]]:
                self.constraints_graph[constraint[1]].append(constraint[0])
            if constraint[1] not in self.constraints_graph[constraint[0]]:
                self.constraints_graph[constraint[0]].append(constraint[1])


    def setProblemFileName(self, name):
        self.problem_file_name = name

    def setVariablesNumber(self, N):
        self.variables = [-1 for i in range(N)]
        self.assigned = [0 for i in range(N)]
        self.constraints_graph = [[] for i in range(N)]
        self.heur_array = [i for i in range(N)]

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
        problem = open(self.problem_file_name, "r")
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

#for heuristics
    def mrvDhSortingFunction(self):
        self.heur_array.sort(key=cmp_to_key(self.mrvDhCMPFunction))

    def mrvDhCMPFunction(self, a, b):
        if(self.assigned[a]>self.assigned[b]):
            return 1
        elif self.assigned[a]<self.assigned[b]:
            return -1
        elif self.assigned[a]==self.assigned[b] and self.assigned[a]==1:
            return 0
        elif self.assigned[a]==self.assigned[b] and self.assigned[a]==0:
            if len(self.domains[a]) > len(self.domains[b]):
                return 1
            elif len(self.domains[a]) < len(self.domains[b]):
                return -1
            else:
                if self.getDh(a) > self.getDh(b):
                    return 1
                elif self.getDh(a) < self.getDh(b):
                    return -1
                else:
                    return 0

    def getDh(self, index):
        dh = 0
        for i in self.constraints_graph[index]:
            if self.assigned[i] == 0:
                dh += 1
        return dh

    def activateHeuristicsMrvDh(self):
        self.heuristic_is_activated=True
        if not self.constraint_graph_is_built:
            self.buildConstraintGraph()
        # self.mrvDhSortingFunction()

    def updateHeuristics(self):
        if self.heuristic_is_activated:
            self.mrvDhSortingFunction()

    def convert_index(self,n):
        #used to not break the code when activating the heuristique cause whith my algorithm when
        #heuristics are activated we need to always get the first element of the array
        if self.heuristic_is_activated:
            return 0
        return n

    def activateAC3(self):
        if not self.constraint_graph_is_built:
            self.buildConstraintGraph()
        self.AC3_is_activated=True

    def solve(self):
        pass

    def get_number_of_iterations(self):
        return self.number_of_iterations

    def log_state(self,depth,currentVar):
        if self.number_of_iterations<1000:
            log=[]
            log.append("Profondeur: {}".format(depth))
            log_var=[]
            for index,val in enumerate(self.variables):
                if self.assigned[index]:
                    log_var.append(val)
                else:
                    log_var.append("*")
            log.append(str(log_var))
            log.append("---domains---")

            for index,k in enumerate(self.domains):
                if currentVar==index:
                    pointer=" ---> "
                else:
                    pointer = "      "
                log.append(str(index)+":"+pointer+str(k))
            log.append("===============================================================")
            logFile=open("log.txt","a")
            logFile.write("\n".join(log)+"\n")
        elif self.number_of_iterations==1000:
            log=[]
            log.append("...")
            log.append("...")
            log.append("...")
            log.append("Nombre d'iterations est tres grand, on ne peut pas le logger ")
            logFile = open("log.txt", "a")
            logFile.write("\n".join(log) + "\n")
# # test
# a = CSP()
# a.parseProblemFromFile()
# a.buildConstraintGraph()
# a.mrvDhSortingFunction()
# print(a.heur_array)
