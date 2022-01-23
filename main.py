from typing import List, Any
from expression import *
from pattern import *

class NLogError(Exception):
    def __init__(self, t):
        super().__init__(self, t)

class Main:
    code = ""
    outCode = ""
    inFile = "in.nlog"
    outFile = "out.mlog"

    patternStart = "{"
    functionStart = "("
    patternInit = "|"
    patternEnd = "}"
    functionEnd = ")"
    mark = "*"

    paramsSeparator = ","
    paramsNull = " "

    expressions: List[Expression] = [
        Expression("read", readL),
        Expression("write", writeL),
        Expression("print", printL),
        Expression("set", setL),
        Expression("wait", waitL),
        Expression("ubind", ubindL),
        Expression("getlink", getLinkL),
        Expression("drawflush", drawFlushL),
        Expression("printflush", printFlushL),
        Expression("draw", drawL),
        Expression("control", controlL),
        Expression("radar", radarL),
        Expression("op", opL),
        Expression("lookup", lookupL),
        Expression("end", endL),
        Expression("jump", jumpL),
        Expression("ucontrol", ucontrolL),
        Expression("uradar", uradarL),
        Expression("ulocate", ulocateL)
    ]
    patterns: List[Pattern] = [
        Pattern("if", ifP)
    ]

    marks = {}

    def __init__(self): self.start()

    def start(self):
        self.read()
        self.clearCode1()
        Main.outCode = self.handleStatments(Main.code)
        self.handlePatterns()
        self.clearCode2()
        self.compile()
        self.clearCode3()
        self.write()

    def read(self):
        Main.code = open(Main.inFile).read()

    def clearCode1(self):
        pass

    def handleStatments(self, string):
        code = ""
        temp = ""
        i = 0
        while i < len(string):
            s = string[i]
            if s != "\n":
                if s != Main.functionStart:
                    if s != Main.mark:
                        temp += 1
                    else:
                        Main.marks[temp] = self.countSymbols(Main.outCode, "\n", e=i) + 1
                else:
                    z = 0
                    prms, offset = self.readBefore(Main.functionEnd, i + 1, string)
                    st = [temp, self.readParams(prms, Main.paramsSeparator)]
                    for expr in Main.expressions:
                        if expr.nlogFunction == temp:
                            out = expr.get(st)
                            if out != "": code += out + "\n"
                            temp = ""
                            i += offset
                            z = 1
                            break
                    if z == 0: temp += s
            else:
                if temp != "": code += temp + "\n"
                temp = ""
            i += 1
        return code

    def handlePatterns(self):
        temp = ""
        i = 0
        while i < len(Main.outCode):
            s = Main.outCode[i]
            if s != Main.patternInit:
                pass
            else:
                pt, offset1 = self.readBefore(Main.functionStart, i + 1, Main.outCode)
                ptPr, offset2 = self.readBefore(Main.functionEnd, i + offset1 + 1, Main.outCode)
                ptPr = self.readParams(ptPr, " ")
                ptCd, offset = self.readBefore(Main.patternEnd, i + offset2 + offset1 + 3, Main.outCode)
                l = offset + offset1 + offset2
                for pattern in Main.patterns:
                    if pattern.initWord == pt:
                        p1 = Main.outCode[:i]
                        p2 = Main.outCode[i+l+4:]
                        codeToPaste = pattern.get(ptPr, ptCd, i, self.countSymbols(Main.outCode, "\n", e=i)+1)
                        Main.outCode = p1 + codeToPaste + p2
                        i += len(codeToPaste) - 1
                        pass
            i += 1

    def clearCode2(self):
        pass

    def compile(self):
        pass


    def clearCode3(self):
        pass

    def write(self):
        q = open(Main.outFile, "w")
        q.write(self.outCode)
        q.close()

    def readBefore(self, a, ind, code):
        temp = ""
        i = ind
        while i < len(code):
            symbol = code[i]
            if symbol != a:
                temp += symbol
            else:
                return temp, i - ind + 1
            i += 1
        raise self.syntaxError(ind)

    def readParams(self, string, sep):
        params: List[str] = []
        temp = ""
        for i in range(len(string)):
            s = string[i]
            if s != sep:
                if s != Main.paramsNull:
                    temp += s
            else:
                params.append(temp)
                temp = ""
        if temp != "": params.append(temp)
        return params

    def countSymbols(self, string, s, e=-1):
        counter = 0
        for i in range(len(string)):
            if e != -1:
                if i == e:
                    break
            if string[i] == s:
                counter += 1
        return counter

    syntaxError = lambda self, ind: NLogError(f"Syntax error at {ind}")

Main()





































































