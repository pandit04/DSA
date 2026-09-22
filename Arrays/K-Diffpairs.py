from collections import Counter

class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0

        freq = Counter(nums)

        if k == 0:
            return sum(1 for num in freq if freq[num] >= 2)

        count = 0

        for num in freq:
            if num + k in freq:
                count += 1

        return count

print(Solution().findPairs([3,1,4,1,5], 2))