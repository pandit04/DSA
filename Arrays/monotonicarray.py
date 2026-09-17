def ismonotonic(nums):
    increasing = True
    decreasing = True

    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            increasing = False
        if nums[i]<nums[i+1]:
            decreasing = False

        return increasing or decreasing

nums = [1,2,2,3,4]
print(ismonotonic(nums))