# Travaille TP2 Projet CSP
# Gastli Oussama
# Hanana Nour
# GL4

variables = {
    "X1": -1,
    "X2": -1,
    "T": -1,
    "W": -1,
    "O": -1,
    "F": -1,
    "U": -1,
    "R": -1


}
domains = {
    "T": [i for i in range(10)],
    "W": [i for i in range(10)],
    "O": [i for i in range(10)],
    "F": [i for i in range(10)],
    "U": [i for i in range(10)],
    "R": [i for i in range(10)],
    "X1": [0, 1],
    "X2": [0, 1]

}

assigned = {
    "T": 0,
    "W": 0,
    "O": 0,
    "F": 0,
    "U": 0,
    "R": 0,
    "X1": 0,
    "X2": 0
}


def check_contraints():
    for i in list(variables.keys()):
        for k in list(variables.keys()):
            if(i!=k and assigned[i] and assigned[k]):
                if i!="X1" and i!="X2" and k!="X1" and k!="X2" and variables[i]==variables[k]:
                    return False
    if (assigned["O"] and assigned["R"] and assigned["X1"]):
        if (2 * variables["O"] != variables["R"] + 10 * variables["X1"]):
            return False
    if (assigned["W"] and assigned["U"] and assigned["X1"] and assigned["X2"]):
        if (2 * variables["W"] + variables["X1"] != variables["U"] + 10 * variables["X2"]):
            return False
    if (assigned["T"] and assigned["O"] and assigned["F"] and assigned["X2"]):
        if (2 * variables["T"] + variables["X2"] != variables["O"] + 10 * variables["F"]):
            return False
    if assigned["F"] and variables["F"]==0:
        return False
    return True


def backTracking(depth: int, keysArray):
    global variables
    global domains
    global assigned
    if (depth == len(variables)):
        return True
    currentKey = keysArray[depth]
    for k in domains[currentKey]:
        assigned[currentKey] = 1
        variables[currentKey] = k
        if check_contraints():
            if backTracking(depth + 1, keysArray):
                return True
        assigned[currentKey] = 0
    return False


keys = list(variables.keys())
ok = backTracking(0, keys)
if ok:
    print(variables)
