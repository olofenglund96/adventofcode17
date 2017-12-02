sum = 0;
with open("../input_files/2") as f:
    for line in f:
        line = line.replace('\t', " ")
        numbers = line.split(" ")
        maxnum = 0;
        minnum = 10000;
        for n in numbers:
            n = int(n)
            if(n > maxnum):
                maxnum = n
            if(n < minnum):
                minnum = n
        print(str(maxnum) + ", " + str(minnum))
        sum += maxnum-minnum
print(sum)
