def has_33(nums):
    for i in range(len(nums)):
        if nums[i]==3 and nums[i+1]==3:
            return True 
            break
    return False 
list = [1,3,3]
print(has_33(list))

'''has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False'''