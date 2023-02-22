n = int(input())
def gen2(n):
    cnt = 0 
    for i in range(n):
        if i%2==0:
            yield i 
for i in gen2(n):
    print (i)


