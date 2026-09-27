class Solution:
    def dfs(self,i, j, nums, track):
        if i<0 or i>= len(nums) or j<0 or j>= len(nums[0]):
            return 
        if nums[i][j] == "X":
            return 
        if track[i][j]==1:
            return
        track[i][j] = 1
        self.dfs(i+1, j, nums, track)
        self.dfs(i, j+1, nums, track)
        self.dfs(i-1, j, nums, track)
        self.dfs(i, j-1, nums, track)

    def solve(self, nums: list[list[str]]) -> None:
        m,n = len(nums), len(nums[0])
        track = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0  or i==m-1 or j ==0 or j == n-1:
                    if nums[i][j]== 'O':
                        if track[i][j] == 0 :
                            self.dfs(i,j, nums, track)

        for i in range(m):
            for j in range(n):
                if track[i][j] == 0 :
                    nums[i][j] = "X"

        