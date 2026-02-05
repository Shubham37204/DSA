class Solution:
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)  
        a = b = 0
        actual_sum = 0
        s = set() 

        for i in range(n):           
            for j in range(n):
                val = grid[i][j]
                actual_sum += val    
                if val in s:         
                    a = val
                s.add(val)

        exp_sum = (n * n * (n * n + 1)) // 2
        b = exp_sum - actual_sum + a
        return [a, b]  

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 8]
]

sol = Solution()
print(sol.findMissingAndRepeatedValues(grid))
