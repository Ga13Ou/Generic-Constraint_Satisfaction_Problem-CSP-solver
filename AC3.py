from CSP import CSP
from copy import deepcopy

class AC3(CSP):

    def reviser(self, i, j):
        deleted = False
        assignValueI,assignValueJ=self.assigned[i],self.assigned[j]
        index1 = 0
        while index1 < len(self.domains[i]):
            go = False
            val1 = self.domains[i][index1]
            for index2, val2 in enumerate(self.domains[j]):
                self.variables[i] = val1
                self.variables[j] = val2
                self.assigned[i] = self.assigned[j] = 1
                if self.checkAllConstraints():
                    go = True
                # cleaning:
                self.assigned[i],self.assigned[j]=assignValueI,assignValueJ
                if go:
                    break
            if not go:
                self.domains[i].pop(index1)
                index1 -= 1
                deleted = True
            index1 += 1
        return deleted

    def AC1(self):
        go = True
        while go:
            go = False
            for i in range(len(self.variables)):
                for j in range(len(self.variables)):
                    if i != j:
                        self.reviser(i, j)

    def rec_reviser(self, i, j):
        if self.assigned[i]*self.assigned[j]==0:
            change = self.reviser(i, j)
            if change:
                for k in self.constraints_graph[i]:
                    self.rec_reviser(i, k)

    def initArcConsistency3(self):
        # called only the first time to get an initial consistincy constraints graph
        for i in range(len(self.constraints_graph)):
            for j in self.constraints_graph[i]:
                self.rec_reviser(i, j)

    def arcConsistency3(self,index):
        for i in self.constraints_graph[index]:
            self.rec_reviser(index,i)

#
# test = AC3()
# test.setProblemFileName("testExample/sudokuProblem.txt")
# test.parseProblemFromFile()
# test.buildConstraintGraph()
# test.arcConsistency3()
# # pprint(test.constraints_array)
# # print(test.constraints_graph)
# print(test.domains)
# print(test.variables)
