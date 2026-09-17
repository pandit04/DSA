# Majority Element (Hash Map / Frequency Count)
# Input: nums = [3, 2, 3]
# Output: 3

def majority_element(nums):
    count = {}
    n = len(nums)

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

        if count[num] > n // 2:
            return num

# Test cases
print(majority_element([3, 2, 3]))
print(majority_element([2, 2, 1, 1, 1, 2, 2]))
print(majority_element([1]))
