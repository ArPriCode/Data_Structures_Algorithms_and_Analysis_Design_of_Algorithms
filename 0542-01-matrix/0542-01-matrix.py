from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        que, m, n = deque(), len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    que.append([i, j])
                else:
                    mat[i][j] = float("inf")
        while que:
            i, j = que.popleft()
            check = [ [i+1, j], [i-1, j], [i, j+1], [i, j-1] ]  
            for r, c in check:
                if 0 <= r < m and 0 <= c < n and mat[r][c] > mat[i][j] + 1:
                    mat[r][c] = mat[i][j] + 1
                    que.append([r, c])
        return mat