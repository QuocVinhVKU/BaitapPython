n = int(input())
a = int(input())
b = int(input())
dem = 0
while(n>0):
    n-=(a)
    a+=b
    dem +=1
print(dem)

# n - a
# n - (a+b)
# n - (a+b+b)
# n - (a+b+b+b)
# f0 = a;
# f1 = b;
# fn = n;

# for i in range(2, n):
#     f0 = f1;
#     f1 = fn;
#     fn = f0 + f1;
