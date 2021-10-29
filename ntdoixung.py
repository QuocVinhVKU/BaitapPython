# t = int(input())
# a = []
# for i in range(t):
#     a.append(int(input()))
# for i in range(t):
#     if ( int(a[i])
#     if check == 1:
#         print("YES")
#     else:
#         print("NO")




n = int(input())
a = []
b = []
for i in range(n):
    a.append(int(input()))
for i in range(len(a)):
    j = 2
    for j in range(max(a)):
        if  a[i] % j == 0:
            b.append(a[i])
print(b)   
for i in range(len(b)-1):
    if (int(b[i])==int(int(b[i-1])+int(b[i+1]))/2):
        print("YES")
    else:
        print("NO")



