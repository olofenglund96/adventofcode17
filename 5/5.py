numbers = []
with open("../input_files/5") as f:
    for line in f:
        line = line.replace("\n", "")
        numbers.append(int(line))

i = 0
index = 0
count = 0
while(i >= 0 and i < len(numbers)):
    count += 1
    index = i
    i += numbers[i]
    numbers[index] += 1

print(count)
