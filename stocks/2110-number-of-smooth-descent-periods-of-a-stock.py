# Solution takes O(n) time and O(1) space

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # Split into descents
        ans = 0
        smooth_len = 1
        for i in range(1, len(prices)):
            if prices[i] == prices[i-1] - 1:
                smooth_len += 1
            else:
                # Count how many ways to split up smooth_len
                ans += (smooth_len + 1) * smooth_len // 2

                # 4 3 2 1
                # 4 3 2
                # 2 3 1
                # 4 3
                # 3 2
                # 2 1
                # 4
                # 3
                # 2
                # 1

                smooth_len = 1

        # Do the same
        ans += (smooth_len + 1) * smooth_len // 2
        return ans