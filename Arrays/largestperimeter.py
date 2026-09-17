def largestperimeter(nums):
    nums.sort()

    for i in range(len(nums)-1,1,-1):
        if nums[i-2]+nums[i-1]>nums[i]:
            return nums[i-2]+nums[i-1]+nums[i]
        return 0

nums =[3,2,3,4]
print(largestperimeter(nums))