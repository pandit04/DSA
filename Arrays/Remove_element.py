#Input: nums = [3, 2, 2, 3], val = 3
#Output: k = 2, nums = [2, 2, _, _]
#Explanation: The function returns k = 2. The first 2 elements of nums are set to 2.

def removeelement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

nums = [3, 2, 2, 3]
val = 3
k = removeelement(nums, val)
print(f"k = {k}, nums = {nums[:k]}")