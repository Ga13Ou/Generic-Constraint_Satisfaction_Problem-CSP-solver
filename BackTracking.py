from CSP import CSP


class BackTracking(CSP):

    def BT(self, index: int):
        if index == len(self.variables):
            return True

        for k in range(len(self.domains[index])):
            self.variables[index] = self.domains[index][k]
            self.assigned[index] = 1
            if (self.checkAllConstraints()):
                if (self.BT(index + 1)):
                    return True
            self.assigned[index] = 0
        return False

    def solve(self):
        self.parseProblemFromFile()
        print("tessst")
        self.BT(0)


# test
a = BackTracking()
# a.setProblemFileName("testExample/mapColoringProblem.txt")
a.setProblemFileName("testExample/problem.txt")
a.solve()
print(a.variables)

# expected="397286541412539768856471329284195637639748215571362894728913456163854972945627183"
# actual="".join(str(x) for x in a.variables)
# print(a.variables)
