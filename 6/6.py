import math

def redist(numbers):
    maxNum = 0
    index = 0
    for i, n in enumerate(numbers):
        if(n > maxNum):
            maxNum = n
            index = i

    numbers[index] = 0
    i = index + 1
    while(maxNum != 0):
        numbers[i%len(numbers)] += 1
        i+=1
        maxNum-=1
    return numbers

def compArrays(numbers):
    cycles = 0
    states = []
    while(True):
        for state in states:
            if(state == numbers):
                return cycles

        states.append(list(numbers))
        numbers = redist(numbers)
        cycles+=1


numbers = []
with open("../input_files/6") as f:
    for line in f:
        nums = [int(n) for n in line.strip("\n").replace("\t", " ").split(" ")]

print(compArrays(nums))
