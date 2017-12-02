import re
discs = []

class Disc:
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent

    def findRoot():
        if(parent != None):
            parent.findRoot()
        else:
            print(self.name)

def findDisc(name):
    for i, disc in enumerate(discs):
        if(disc.name == name):
            return i
    return -1

def parseLine(line):
    tempDiscs = re.findall("[a-z]\w+", line)
    parent = tempDiscs[0]
    if(findDisc(parent) == -1):
        discs.append(Disc(parent))

    if(len(tempDiscs) != 1):
        for i in range(1, len(tempDiscs)):
            di = findDisc(tempDiscs[i])
            if(di == -1):
                discs.append(Disc(tempDiscs[i], parent))
            else:
                discs[di].parent = parent

def findRoot():
    for disc in discs:
        if(disc.parent == None):
            print(disc.name)


with open("../input_files/7") as f:
    for line in f:
        parseLine(line)

    findRoot()
