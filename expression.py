class Expression:
    def __init__(self, nf, func):
        self.nlogFunction = nf
        self.function = func

    def get(self, l, args):
        return self.function(l, args=[])

class Params:
    pass

def readL(line, args):
    temp = ""
    if len(line[1]) != 3: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def writeL(line, args):
    temp = ""
    if len(line[1]) != 3: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def printL(line, args):
    temp = ""
    if len(line[1]) != 1: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def setL(line, args):
    temp = ""
    if len(line[1]) != 2: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def waitL(line, args):
    temp = ""
    if len(line[1]) != 1: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def ubindL(line, args):
    temp = ""
    if len(line[1]) != 1: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def getLinkL(line, args):
    temp = ""
    if len(line[1]) != 2: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def drawFlushL(line, args):
    temp = ""
    if len(line[1]) != 1: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def printFlushL(line, args):
    temp = ""
    if len(line[1]) != 1: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def drawL(line, args):
    temp = ""
    if len(line[1]) != 7: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def controlL(line, args):
    temp = ""
    if len(line[1]) != 6: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def radarL(line, args):
    temp = ""
    if len(line[1]) != 7: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def sensorL(line, args):
    temp = ""
    if len(line[1]) != 3: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def opL(line, args):
    temp = ""
    if len(line[1]) != 4: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def lookupL(line, args):
    temp = ""
    if len(line[1]) != 3: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def endL(line, args):
    temp = ""
    if len(line[1]) != 0: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def jumpL(line, args):
    temp = ""
    if len(line[1]) != 4: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def ucontrolL(line, args):
    temp = ""
    if len(line[1]) != 6: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def uradarL(line, args):
    temp = ""
    if len(line[1]) != 7: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp

def ulocateL(line, args):
    temp = ""
    if len(line[1]) != 8: raise TypeError("Arguments error")
    temp += line[0]
    for i in line[1]:
        temp += " "
        temp += i
    return temp
