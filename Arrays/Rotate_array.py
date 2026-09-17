def rotatearray(nums,k):
    k= k % len(nums)
    
    last_part =nums[-k:]
    first_part = nums[:-k]

    rotate_array = last_part + first_part
    nums[:]=rotate_array

    return nums


nums=[1,2,3,4,5,6,7]
k=3
print(rotatearray(nums,k))