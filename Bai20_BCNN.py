def uscln(a, b):
    while ( a != b):
        if (a > b):
            a = a - b;
        else:
            b = b - a;
    return a
def bscnn(a, b):
    return int((a * b) / uscln(a, b));
x = input()
x = x.split()
a = int(x[0])
b = int(x[1])
print(uscln(a,b), end=' ')
print(bscnn(a,b))