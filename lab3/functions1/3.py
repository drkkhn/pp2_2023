def solve(numheads,numlegs):
    chicken = ((numheads * 4)-numlegs)/2
    rabbit = numheads - chicken
    print (int(chicken),int(rabbit))
h,l = map(int,input().split())
solve(h,l)
