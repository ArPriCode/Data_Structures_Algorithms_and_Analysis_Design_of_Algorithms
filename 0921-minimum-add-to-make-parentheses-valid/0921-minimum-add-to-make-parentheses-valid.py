class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        min_add = 0
        valid = 0

        for c in s:
            if c == '(':
                valid += 1
            else:
                if valid == 0:
                    min_add += 1
                else:
                    valid -= 1

        return min_add + valid