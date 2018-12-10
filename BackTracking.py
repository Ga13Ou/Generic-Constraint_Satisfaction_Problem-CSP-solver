# Travaille TP2 Projet CSP
# Gastli Oussama
# Hanana Nour
# GL4



from AC3 import AC3
from copy import deepcopy


class BackTracking(AC3):

    def BT(self, index: int):
        ac_result=True #this line used in case of the ac3 is not activated so we can pass the test of the recursive call
        if index == len(self.variables):
            return True
        heurIndex = self.convert_index(index)
        self.updateHeuristics()
        for k in range(len(self.domains[self.heur_array[heurIndex]])):
            self.number_of_iterations += 1
            self.variables[self.heur_array[heurIndex]] = self.domains[self.heur_array[heurIndex]][k]
            self.assigned[self.heur_array[heurIndex]] = 1 #Save
            heur_array_copy=deepcopy(self.heur_array)
            currentVarDomainCopy = deepcopy(self.domains[self.heur_array[heurIndex]])
            self.domains[self.heur_array[heurIndex]] = [self.variables[self.heur_array[heurIndex]]]
            domainsCopy=deepcopy(self.domains)
            if self.AC3_is_activated:
                ac_result = self.arcConsistency3(self.heur_array[heurIndex])
            self.log_state(index,self.heur_array[heurIndex])
            if (self.AC3_is_activated or self.checkAllConstraints()):
                #todo trying a new verification here
                if ac_result:
                    if (self.BT(index + 1)):
                        return True
            self.assigned[self.heur_array[heurIndex]] = 0 #Restore
            self.heur_array=heur_array_copy
            self.domains=domainsCopy
            self.domains[self.heur_array[heurIndex]] = currentVarDomainCopy
        return False

    def solve(self):
        if self.AC3_is_activated:
            self.initArcConsistency3()
            print("initialisation de l'arc consistance avec succes")
        return self.BT(0)

