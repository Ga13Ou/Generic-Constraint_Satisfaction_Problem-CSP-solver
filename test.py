# s="007206501410000000050470020080095607009040010001302000720900006003000072940600080"
# for i in range(len(s)):
#     if s[i]=="0":
#         print("[1,2,3,4,5,6,7,8,9]")
#     else:
#         print("[{}]".format(int(s[i])))


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


aff=[]
for i in range(81):
    for j in range(i+1,81):
        if(i!=j):
            if(ligne(i)==ligne(j) or colone(i)== colone(j) or carre(i) == carre(j)):
                print("diff;{};{}".format(i,j))