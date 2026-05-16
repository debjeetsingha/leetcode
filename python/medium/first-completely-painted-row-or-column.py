"""
LEETCODE 2661
LINK: https://leetcode.com/problems/first-completely-painted-row-or-column/
"""

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        
        pos = {}
        for x in range(n):
            for y in range(m):
                pos[mat[x][y]] = (x,y)
        
        row_count = [0] * n
        col_count = [0] * m

        for i, num in enumerate(arr):
            x,y = pos[num]

            row_count[x] += 1
            col_count[y] += 1

            if row_count[x]==m:
                return i
            if col_count[y]==n:
                return i
        
        return -1