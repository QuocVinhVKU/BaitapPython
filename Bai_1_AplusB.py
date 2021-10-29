n= int(input())
a = []
for i in range(n):
    s = input()
    s = s.split()
    b = int(s[0])+int(s[1])
    a.append(b)
    
print ('\n'.join(map(str, a)))


