n = input()
dem = 0
a = list(n)
a.reverse()
for i in range(len(a)-1,-1,-1):
    dem += (int(a[i]))*(2**i)
print(dem)