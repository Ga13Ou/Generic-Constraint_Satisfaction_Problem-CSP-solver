from CSP import CSP
from copy import deepcopy

class AC3(CSP):

    def reviser(self, i, j,ok):
        deleted = False
        if ok:
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
                    if len(self.domains[i])==0:
                        # if one domain gets empty no need to continue the processing because it means that this can't contain a solution
                        ok=False
                        break
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
        ok=True
        if self.assigned[i]*self.assigned[j]==0:
            change = self.reviser(i, j,ok)
            if not ok:
                return ok
            if change:
                for k in self.constraints_graph[i]:
                    self.rec_reviser(i, k)
        return ok

    def initArcConsistency3(self):
        go=True
        # called only the first time to get an initial consistincy constraints graph
        for i in range(len(self.constraints_graph)):
            for j in self.constraints_graph[i]:
                go=self.rec_reviser(i, j)
                if not go:
                    break
        return go

    def arcConsistency3(self,index):
        go=True
        for i in self.constraints_graph[index]:
            go=self.rec_reviser(index,i)
            if not go:
                break
        return go
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
