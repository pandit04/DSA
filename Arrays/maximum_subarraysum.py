# Maximum Subarray (Prefix Sum Approach)
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6

def max_subarray(nums):
    prefix_sum = 0
    min_prefix = 0
    max_sum = float('-inf')

    for num in nums:
        prefix_sum += num
        current_sum = prefix_sum - min_prefix
        max_sum = max(max_sum, current_sum)
        min_prefix = min(min_prefix, prefix_sum)

    return max_sum

# Test cases
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray([1]))
print(max_subarray([5, 4, -1, 7, 8]))
print(max_subarray([-1]))
