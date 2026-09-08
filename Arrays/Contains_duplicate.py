#contains Duplicate
#[1,3,2,3]

def containduplicta(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums [j]:
                return True
    return False
         
nums =[1,3,2,3]
print(containduplicta(nums))
