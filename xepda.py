from typing import Match


import math
n = int(input())
b = 0
c = 2147483648
s=-1
for i in range(round(math.sqrt(n))):
    # print(round(math.sqrt(n)))
    for j in range(round(math.sqrt(n))):
        if (i*j >= n):
            a=int(i)
            b=int(j)
            c=(int(i+j)*2)
            
print("'Kich thuoc: '" + str(a) +" "+str(b))