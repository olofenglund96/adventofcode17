def declarePass(words):
    for word in words:
        matches = 0;
        for comp in words:
            if(word == comp):
                matches+=1
                if(matches > 1):
                    return False
    return True
passes = 0
with open("../input_files/4") as f:
    for line in f:
        line = line.replace("\n", "")
        words = line.split(" ")
        if(declarePass(words)):
            passes +=1
            
print(passes)
