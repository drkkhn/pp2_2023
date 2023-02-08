def spy_game(nums):
    cnt = 0 
    for i in range(len(nums)) :
        if (nums[i] == 0) or (nums[i]==7) :
            cnt+=1
    if cnt == 3 :
        return True 
    return False 
spy = [1,2,4,0,0,7,5]
print (spy_game(spy))
'''spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False'''