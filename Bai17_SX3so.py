import math
n = int(input())
check = False
for i in range(2,round(math.sqrt(n)+1)):
    if i**2 == n:
        check = True
        break
if (check==True):
    print("YES")
else: print("NO")

