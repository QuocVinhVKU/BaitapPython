lst = []
a = input()

for i in range(len(lst)):
    for j in range(i):
        if int(lst[i]) < int(lst[j]):
            tmp = int(lst[i])
            int(lst[i]) = int(lst[j])
            int(lst[j]) = tmp
print(lst)