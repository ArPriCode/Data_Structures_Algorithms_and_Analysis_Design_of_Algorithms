class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up_sequence = 0
        down_sequence = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]: 
                up_sequence = down_sequence + 1
            elif nums[i] < nums[i+1]:
                down_sequence = up_sequence + 1
        return 1 + max(up_sequence, down_sequence)