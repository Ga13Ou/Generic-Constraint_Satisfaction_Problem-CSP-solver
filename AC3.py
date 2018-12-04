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

    def eqVerifier(self,i,j):
        return self.variables[i] == self.variables[j]

    def sameDiagonalVerifier(self,i,j):
        return abs(i-j) == abs(self.variables[i]-self.variables[j])

    def notSameDiagonalVerifier(self,i,j):
        return not self.sameDiagonalVerifier(i,j)

