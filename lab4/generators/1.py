n = int(input())
def gen1(n):
    for i in range(n):
        if i**2 <= n :
            yield i**2
for i in gen1(n):
    print (i)   