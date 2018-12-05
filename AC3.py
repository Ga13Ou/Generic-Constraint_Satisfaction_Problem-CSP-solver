from CSP import CSP


class AC3(CSP):

    def reviser(self, i, j):
        deleted = False
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
                self.assigned[i] = self.assigned[j] = 0
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
        change = self.reviser(i, j)
        if change:
            for k in self.constraints_graph[i]:
                self.rec_reviser(i, k)

    def arcConsistency3(self):
        for i in range(len(self.constraints_graph)):
            for j in self.constraints_graph[i]:
                self.rec_reviser(i, j)


test = AC3()
test.parseProblemFromFile()
test.buildConstraintGraph()
test.arcConsistency3()
# pprint(test.constraints_array)
# print(test.constraints_graph)
print(test.domains)
print(test.variables)
