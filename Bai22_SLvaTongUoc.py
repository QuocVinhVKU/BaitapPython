n = int(input())
a= []
dem=0
for i in range(1, n+1):
    if n%i==0:
        dem+=1
        a.append(i)
# print (' '.join(map(str,a)), end=' ' )
tong = 0
for i in range(len(a)):
    tong+=a[i]
print(dem, end=' ')
print(tong)
