from copy import deepcopy
class ForwardChecking:
    def __init__(self):
        self.variables=[]
        self.assigned=[]
        self.domains=[]
        
    def setDomains(self,array):
        self.domains=array

    def setVariables(self,number):
        self.variables=[-1 for i in range(number)]
        self.assigned=[0 for i in range(number)]

    def constraints(self,currentIndexVariable,varArray,varDomain):
        for j in range(len(varArray)):
            if(self.assigned[j]==1):
                if((abs(varArray[j]-varArray[currentIndexVariable])== abs(j-currentIndexVariable)) or (varArray[j]==varArray[currentIndexVariable])):
                    return False
        return True

    def FC(self,varIndex:int,varArray:list,varDomain):
        for i in range(varIndex+1,len(self.variables)):
            k=0
            while(k<len(varDomain[i])):
                varArray[i]=varDomain[i][k]
                if(not self.constraints(i,varArray,varDomain)):
                    varDomain[i].pop(k)
                    k-=1
                k+=1
            if(len(varDomain[i])==0):
                #this is when the domain gets empty after FC
                return False
        return True


    def forwardSolver(self,currentIndex,varArray,varDomain):
        if(currentIndex==len(self.variables)):
            self.variables=varArray
            self.domains=varDomain
            return True
        for value in varDomain[currentIndex]:
            varArray[currentIndex]=value
            self.assigned[currentIndex]=1
            varArrayCopy=deepcopy(varArray)
            varDomainCopy=deepcopy(varDomain)
            if(self.FC(currentIndex,varArrayCopy,varDomainCopy)):
                if(self.forwardSolver(currentIndex+1,varArrayCopy,varDomainCopy)):
                    return True
            self.assigned[currentIndex]=0
        return False

    def solver(self):
        return self.forwardSolver(0,self.variables,self.domains)



# test
a=[[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7]]
resolver=ForwardChecking()

resolver.setDomains(a)
resolver.setVariables(8)

ok=resolver.solver()
if(ok):
    print(resolver.variables)
    print(resolver.domains)