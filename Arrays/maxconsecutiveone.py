def maxconsecutiveone(nums):

    count = 0 
    max_count = 0
     
    for i in nums:
        if i == 1:
            count +=1
            max_count= max(count,max_count)
        else:
            count =0
    return max_count

nums = [1,1,0,1,1,1]
print(maxconsecutiveone(nums))

