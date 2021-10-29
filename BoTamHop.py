n = int(input())
a = (input().split())
a.sort()
c = []
dem = 0
d = []
for i in range(n):
    for j in range(i+1,n):
        c.append(int(a[i])+int(a[j]))
for i in range(n):
    for j in range(len(c)):
        if (int(a[i])==int(c[j])/2):
            dem += 1
            d.append(int(a[i])+int(c[j]))
print(dem, end="\n")
print(max(d))
