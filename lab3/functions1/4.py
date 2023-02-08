import cmath 
def filter_prime(LList):
    ans = []
    for i in LList:
        if i == 1 :
            continue
        if i == 2 : 
            ans.append(2) 
            continue
        cnt = 0
        for j in range(2,i):
            if (i%j==0):
                cnt += 1
        if (cnt == 0):
            ans.append(i)
    return ans 
n = [1,2,3,4,5,6,7,8,9,10]
print (filter_prime(n))   
        

         

