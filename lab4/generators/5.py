n = int(input())
def gen5(n):
    for i in range(n,-1,-1):
        yield i 
for i in gen5(n):
    print (i)