class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        ans = 1
        inc = 1
        dec = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i-1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
                
            if inc > ans:
                ans = inc
            if dec > ans:
                ans = dec
                
        return ans