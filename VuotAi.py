n = input().split()
a = input().split()
a = list(map(int, a))
k = int(n[1])
ans = 0
for i in range(len(a)):
	if max(a)>=k: ans = sum(a)-k+1
	else:
    		ans = sum(a)-max(a)+1
print(ans)	
