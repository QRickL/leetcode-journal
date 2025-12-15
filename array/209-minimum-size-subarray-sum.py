# O(n) time
# O(1) space

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        right = 0

        cur = nums[0]
        ans = 100000 + 1

        while (right < len(nums)):

            if cur < target:
                right += 1
                if right >= len(nums):
                    break
                cur += nums[right]
            else:
                ans = min(right - left + 1, ans)
                left += 1
                cur -= nums[left-1]

        if ans == 100000 + 1:
            ans = 0

        return ans