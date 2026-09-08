#remove duplicate
#[0,0,1,1,1,2,2,4]

def removeduplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return removeduplicate(nums[j:])
    return nums

nums = [0,0,1,1,1,2,2,4]
print(removeduplicate(nums))