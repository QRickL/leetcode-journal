class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        seen_mod = dict()
        seen_mod[0] = -1
        cur = 0

        for i in range(len(nums)):
            # if nums[i] % k == 0:
            #     continue
            cur += nums[i]
            cur = cur % k

            if cur in seen_mod:
                if (i - seen_mod[cur] >= 2):
                    return True
            else:
                seen_mod[cur] = i

        return False