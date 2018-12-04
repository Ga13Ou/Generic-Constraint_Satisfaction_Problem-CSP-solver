

def  constraint(currentIndex):
    # print("[log]: index={}, queens[index]={}".format(currentIndex,queens[currentIndex]))
    for j in range(currentIndex):
        if((abs(queens[j]-queens[currentIndex])== abs(j-currentIndex)) or (queens[j]==queens[currentIndex])):
            # print("\t[log]: j={}, queens[j]={}".format(j,queens[j]))
            return False
    return True

def beautifulprint(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if(j != array[i]):
                print(" |",end=" ",flush=True)
            else:
                print("o|",end=" ",flush=True)
        print("\n")



N=int(input("tapez N: "))
queens=[-1 for i in range(N)]
i=0
while(i>=0 and i<N):
    if(queens[i]<N-1):
        queens[i]+=1
        ok=constraint(i)
        if(ok):
            i+=1
    else:
        i-=1
        for k in range(i+1,N):
            queens[k]=-1
print(queens)
if(i==0):
    print("No Solution")
elif(i==N):
    print("there is a solution",queens)
    beautifulprint(queens)

