"""class SpiralCell:
    x = 0
    y = 0
    val = 0

    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
"""
import math

def produceResult():
    print(math.fabs(x) + math.fabs(y));

x = 0
y = 0
val = 0
inp = 289326
i = 0
rowLen = math.ceil(math.sqrt(inp))+1
val = pow(rowLen, 2);
x = math.floor(rowLen/2)
y = -x
print(val)

for i in range(0, rowLen-1):
    if(val != inp):
        val-=1
        x-=1
    else:
        produceResult()
        break
y+=1
for i in range(0, rowLen-1):
    if(val != inp):
        val-=1
        y+=1
    else:
        produceResult()
        break
x+=1
for i in range(0, rowLen-1):
    if(val != inp):
        val-=1
        x+=1
    else:
        produceResult()
        break
y-=1
for i in range(0, rowLen-1):
    if(val != inp):
        val-=1
        y-=1
    else:
        produceResult()
        break
