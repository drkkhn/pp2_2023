n = int(input())
def gen3(n):
    for i in range(n):
        if i%3==i%4==0:
            yield i 
for i in gen3(n):
    print (i)
print(type(gen3))