from CSP import CSP


class BackTracking(CSP):

    def BT(self, array: list, d: list, index: int):
        if (len(array) == 0):
            return True

        for k in range(len(d[0])):
            array[0] = d[0][k]
            self.variables[index] = array[0]
            self.assigned[index]=1
            if (self.checkAllConstraints()):
                if (self.BT(array[1:], d[1:], index + 1)):
                    return True
            self.assigned[index]=0
        return False

    def solve(self):
        self.parseProblemFromFile()
        print("tessst")
        self.BT(self.variables,self.domains,0)


# test
a=BackTracking()
# a.setProblemFileName("testExample/mapColoringProblem.txt")
a.setProblemFileName("testExample/NqueenProblem.txt")
a.solve()
print(a.variables)

# expected="397286541412539768856471329284195637639748215571362894728913456163854972945627183"
# actual="".join(str(x) for x in a.variables)
# print(a.variables)