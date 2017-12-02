sum = 0;
input = "";
with open("../input_files/1") as f:
    for c in f:
        input += c;

    print(input)
    for i in range(0, len(input)-1):
        if(input[i] == input[i+1]):
            sum += int(input[i])

    sum += 6

print(sum)
