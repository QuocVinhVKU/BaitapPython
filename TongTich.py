b = input()
a = input()
a = a.split()
b = b.split()
c = int(b[0])
d = int(b[1])
dem = 0
for i in range(c):
    ai = int(a[i])
    for j in range(c):
        aj = int(a[j])
        if (i<j and (int((ai+aj)%d) == int((ai*aj)%d))):
            dem += 1
print(dem)
