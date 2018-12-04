
# class Solver:
#     def __init__(self)
from pprint import pprint
import copy


variables=[]
domains=[]

def init(N):
    global variables
    global domains
    variables=[0]*N
    domains=[[] for i in range(N)]
    for i in range(N):
        domains[i].extend(list(range(N)))  

def  constraint(currentIndex):
    # print("[log]: index={}, queens[index]={}".format(currentIndex,queens[currentIndex]))
    for j in range(currentIndex):
        if((abs(variables[j]-variables[currentIndex])== abs(j-currentIndex)) or (variables[j]==variables[currentIndex])):
            # print("\t[log]: j={}, queens[j]={}".format(j,queens[j]))
            return False
    return True

def backtracking(array:list,d:list,index:int):
    global variables
    global domains
    if(len(array)==0):
        return True
    for k in range(len(d[0])):
        array[0]=d[0][k]
        variables[index]=array[0]
        if(constraint(index)):
            if(backtracking(array[1:],d[1:],index+1)):
                return True
    return False

def beautifulprint(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if(j != array[i]):
                print(" |",end=" ",flush=True)
            else:
                print("o|",end=" ",flush=True)
        print("\n")


N=int(input("tapez N: "))
init(N)
ok=backtracking(variables,domains,0)
print(ok)
print(variables)

if(ok):
    beautifulprint(variables)





# init(5)
# print(variables)
# # print(domains)
# pprint(domains)