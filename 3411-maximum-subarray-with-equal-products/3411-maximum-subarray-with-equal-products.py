import math
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 2
        for i in range(n):
            p = g = l = nums[i]
            for j in range(i + 1, n):
                p *= nums[j]
                g = math.gcd(g, nums[j])
                l = math.lcm(l, nums[j])
                if p == g * l:
                    ans = max(ans, j - i + 1)
        return ans