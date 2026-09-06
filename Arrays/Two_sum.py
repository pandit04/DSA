#Input: nums = [2, 7, 11, 15],
# target = 9
#Output: [0, 1]

def twosum(nums,target):
    n= len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return[i,j]

print(twosum([2,7,11,15],9))
