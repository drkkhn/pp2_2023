def uniq(list):
    mp = {}
    ans = []
    for i in list:
        mp.setdefault(i,0)
        mp[i]+=1
    for i,j in mp.items():
        if j==1:
            ans.append(i)
    print(ans)
l = [1,2,2,3,4,4,5,5,5,6,7,7,8,9,10]
#ans = [1, 3, 6, 8, 9, 10]
uniq(l)
        