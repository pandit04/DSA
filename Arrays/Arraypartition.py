def arraypartation(nums):
    nums.sort()

    total = 0
    for i in range(0,len(nums),2):
        total = total + nums[i]

    return total

print(arraypartation([6,2,6,5,1,2]))