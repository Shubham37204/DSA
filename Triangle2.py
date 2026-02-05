# 01
# 012
# 0123
#for i in range(1,4):
    # for j in range(i+1):
    #     print(j, end="")
    # print()

# 1
# 12
# 123 
# 1234

for i in range(4):
    for j in range(1,i+1):
        print(j, end="")
    print()

"""
Problem: Incrementing Triangle Pattern

Statement:
Given an integer n, create a triangle pattern where:

- Each row i contains numbers from 1 to i
- The pattern forms a left-aligned triangle
- Numbers increase from 1 up to the row index for each row
- The goal is to print the incrementing triangle pattern

Return the printed pattern in the console.

Example for n=4:
1
12
123
1234
"""

from typing import List

class Solution:
    def incrementingTriangle(self, n: int) -> List[str]:
        """
        Generate incrementing triangle pattern with numbers.
        
        Args:
            n: Number of rows
            
        Returns:
            List of strings representing each row
            
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        result = []
        
        for i in range(1, n + 1):
            row = ""
            for j in range(1, i + 1):
                row += str(j)
            result.append(row)
        
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    output = sol.incrementingTriangle(4)
    for row in output:
        print(row)