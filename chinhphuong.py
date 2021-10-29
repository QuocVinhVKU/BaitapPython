a = int(input())
b = int(input())
c = []
for i in range(a, b):
    
    check = False
    # print (i)
    if (i**2 == b):
        c.append(i)
    
print(c)
