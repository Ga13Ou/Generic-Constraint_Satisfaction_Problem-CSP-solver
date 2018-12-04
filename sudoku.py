variables=[]
domains=[]
modifiable=[]
def init(N):
    global variables
    global domains
    global modifiable
    variables=[0]*81
    modifiable=[0]*81
    variables=list("007206501410000000050470020080095607009040010001302000720900006003000072940600080")
    for letter in range(len(variables)):
        if(variables[letter]=='0'):
            modifiable[letter]=1
    domains=[[] for i in range(81)]
    for i in range(81):
        domains[i].extend(list(range(1,N+1)))
        for j in range(len(domains[i])):
            domains[i][j]=str(domains[i][j])


def ligne(position:int):
    return position // 9
def colone(position:int):
    return position % 9

def carre(position:int):
    l=ligne(position)
    c=colone(position)
    a=l//3
    b=c//3
    return a*3+b

def constraints(currentIndex):
    for j in range(currentIndex):
        if((variables[j]==variables[currentIndex])and ((colone(currentIndex)==colone(j)) or (ligne(currentIndex)==ligne(j)) or (carre(currentIndex)==carre(j)))):
            return False
    for k in range(currentIndex,81):
        if(modifiable[k]==0):
            if((variables[k]==variables[currentIndex])and ((colone(currentIndex)==colone(k)) or (ligne(currentIndex)==ligne(k)) or (carre(currentIndex)==carre(k)))):
                return False
    return True

def BT(array:list,d:list,index:int):
    global variables
    global domains
    if(len(array)==0):
        return True
    if(modifiable[index]==1):
        for k in range(len(d[0])):
            array[0]=d[0][k]
            variables[index]=array[0]
            if(constraints(index)):
                if(BT(array[1:],d[1:],index+1)):
                    return True
    else:
        return BT(array[1:],d[1:],index+1)
    return False

init(9)
ok=BT(variables,domains,0)
print(ok)
print("".join(variables))
# print("397286541412539768856471329284195637639748215571362894728913456163854972945627183")
# print(modifiable)
# print(ligne(11))
# print(colone(11))
# print(carre(18))
# print(domains)
