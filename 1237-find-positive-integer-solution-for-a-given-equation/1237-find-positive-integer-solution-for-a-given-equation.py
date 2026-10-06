"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        x = 1
        l, r = 1, 1000
        while l <= r:
            m = (l + r) // 2
            cur = customfunction.f(m, 1000)
            if cur < z:
                l = m + 1
            elif cur > z:
                r = m - 1
                x = m
            else:
                x = m
                break
        while x < 1001 and customfunction.f(x, 1) <= z:
            l, r = 1, 1000
            while l <= r:
                m = (l + r) // 2
                cur = customfunction.f(x, m)
                if cur < z:
                    l = m + 1
                elif cur > z:
                    r = m - 1
                else:
                    res.append([x, m])
                    break
            x += 1
        return res