n = int(input())
N = input().split()
Q = int(input())
a = []
dem = 0
for i in range(Q):
    a.append(int(input()))
for i in range(Q):
    for j in range(n):
        if(int(N[j])<a[i]):
            dem+=1
    print(dem, end="\n")
    dem = 0

