class BackTracking:
    variables=[]
    domains=[]
    def setDomains(self,array):
        self.domains=array

    def setVariables(self,number):
        self.variables=[-1 for i in range(number)]

    def constraints(self,currentIndexVariable):
        for j in range(currentIndexVariable):
            if((abs(self.variables[j]-self.variables[currentIndexVariable])== abs(j-currentIndexVariable)) or (self.variables[j]==self.variables[currentIndexVariable])):
                # print("\t[log]: j={}, queens[j]={}".format(j,queens[j]))
                return False
        return True

    def BT(self,array:list,d:list,index:int):
        if(len(array)==0):
            return True
        
        for k in range(len(d[0])):
            array[0]=d[0][k]
            self.variables[index]=array[0]
            if(self.constraints(index)):
                if(self.BT(array[1:],d[1:],index+1)):
                    return True
        return False


# test
a=[[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7]]
resolver=BackTracking()

resolver.setDomains(a)
resolver.setVariables(8)

ok=resolver.BT(resolver.variables,resolver.domains,0)
if(ok):
    print(resolver.variables)