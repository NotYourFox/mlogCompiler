class Pattern:
    def __init__(self, initWord, f):
        self.initWord = initWord
        self.func = f

    def get(self, params, inCode, ind, line):
        return self.func(params, inCode, ind, line)

class Params:
    ifInstructionList = {"!=": "notEqual",
                         "==": "equal",
                         "<": "lessThan",
                         "<=": "lessThanEq",
                         ">": "greaterThan",
                         ">=": "greaterThanEq",
                         "===": "strictEqual",
                         "always": "always"}

def countSymbols(string, s, e=-1):
    counter = 0
    for i in range(len(string)):
        if e != -1:
            if i == e:
                break
        if string[i] == s:
            counter += 1
    return counter

def ifP(params, inCode, ind, line):
    mainTo = line + 1
    elseTo = line + countSymbols(inCode, "\n") + 1
    code = inCode

    mainPart = str(mainTo) + " " + Params.ifInstructionList[params[1]] + " " + params[0] + " " + params[2]
    elsePart = str(elseTo) + " always 0 0"
    pattern = f"\
jump {mainPart}\n\
jump {elsePart}\n\
{code}"
    return pattern