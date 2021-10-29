def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);
x = input()
x = x.split()
a = int(x[0])
b = int(x[1])
print(uscln(a,b))