import itertools
def func5(str):
    ans = [''.join(i) for i in itertools.permutations(str)]
    for i in ans :
        print (i,end=" ")
s = input()
func5(s)