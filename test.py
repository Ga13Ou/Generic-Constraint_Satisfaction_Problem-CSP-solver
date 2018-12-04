def oper(a,b):
    return a<b


a = [[[1,2],oper],[[75,4],oper]]
for c in a:
    print(c[1](c[0][0],c[0][1]))