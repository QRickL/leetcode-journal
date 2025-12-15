# O(n) time
# O(n) space

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        prev = dict()
        prev[0] = -1
        ans = 0
        diff = 0

        for i in range(len(nums)):

            diff += (1 if nums[i] == 1 else -1)

            if diff in prev:
                cand = i - prev[diff]
                ans = max(ans, cand)
            else:
                prev[diff] = i
        
        return ans