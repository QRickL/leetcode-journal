# Solution is O(n) time and O(n) size
# O(n) size since a list generates at worst n unique partial sums

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        seen = dict()   # int -> int
        seen[0] = 1
        cur = 0
        ans = 0

        for i in range(len(nums)):
            cur += nums[i]

            if (cur - k) in seen:
                # this means diff is k
                ans += seen[cur - k]
            
            if cur in seen:
                seen[cur] += 1
            else:
                seen[cur] = 1

        return ans