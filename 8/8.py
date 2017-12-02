regs = []
instr = []
max_total = 0

class Registry:
    def __init__(self, name, value):
        self.name = name
        self.value = int(value)

class Instruction:
    def __init__(self, oname, operand, ovalue, cname, condition, cvalue):
        self.oname = findRegistry(oname)
        self.operand = operand
        self.ovalue = int(ovalue)
        self.condition = condition
        print("Instr: " + cname)
        self.cname = findRegistry(cname)
        self.cvalue = int(cvalue)

        if(self.oname == None or self.cname == None):
            raise ValueError("No registry found")

    def checkCondition(self):
        if(self.condition == ">"):
            if(self.cname.value > (self.cvalue)):
                self.performOperation()
        elif(self.condition == "<"):
            if(self.cname.value < (self.cvalue)):
                self.performOperation()
        elif(self.condition == ">="):
            if(self.cname.value >= (self.cvalue)):
                self.performOperation()
        elif(self.condition == "<="):
            if(self.cname.value <= (self.cvalue)):
                self.performOperation()
        elif(self.condition == "=="):
            if(self.cname.value == (self.cvalue)):
                self.performOperation()
        elif(self.cname.value != self.cvalue):
            self.performOperation()

    def performOperation(self):
        global max_total
        if(self.operand == "inc"):
            self.oname.value += self.ovalue
        else:
            self.oname.value -= self.ovalue

        if(self.oname.value > max_total):
            max_total = self.oname.value

    def toString(self):
        return (self.oname.name + " " + self.operand + " " +
                self.ovalue + " " + self.condition + " " +
                self.cname.name + " " + self.cvalue)

def findMaxRegistry():
    maxval = 0
    for reg in regs:
        if(reg.value > maxval):
            maxval = reg.value
    return maxval

def findRegistry(name):
    for reg in regs:
        if(reg.name == name):
            return reg
    return None

def appendIfDistinct(entry):
    for reg in regs:
        if(entry == reg.name):
            return
    regs.append(Registry(entry, 0))

def appendInstruction(entrys):
    instr.append(Instruction(entrys[0],
                entrys[1],
                entrys[2],
                entrys[4],
                entrys[5],
                entrys[6]))

def printInstr():
    for inst in instr:
        print(inst.toString())

def printRegs():
    for reg in regs:
        print(reg.name)

with open("../input_files/8") as f:
    tempInstr = []
    max_total = 0
    for line in f:
        appendIfDistinct(line.split(" ")[0])
        tempInstr.append(line.replace("\n", "").split(" "))

    for inst in tempInstr:
        appendInstruction(inst)


    for inst in instr:
        inst.checkCondition()

    #printRegs()
    #printInstr()
    print(max_total)
