# a = []
# b = []
# n = int(input())
# for i in range(n):
#     book = str(input())
#     author = str(input())
#     year = int(input())
#     price = int(input())
#     gg = 0
#     if price >= 200000:
#         gg = price - 10000
#     else: gg = price - 5000
#     add = book, price, gg
#     a.append(add)

# print(a)
a = []
n = int(input())
for i in range(n):
    book = str(input())
    author = str(input())
    year = int(input())
    price = int(input())
    gg = 0
    if price >= 200000:
        gg = price - 10000
    else: gg = price - 5000
    add= book , price , gg
    a.append('\n'.join(map(str,add)))
print ('\n'.join(map(str,a)) )


    
    


