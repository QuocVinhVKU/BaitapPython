n = int(input())
dem = 0
if n%2==0:
    n-=1
for i in range(round((n-1)/2)):
    dem+=1
print(dem)
