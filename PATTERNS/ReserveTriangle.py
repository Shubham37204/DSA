# 1
# 21
# 321
# 4321

for i in range(1, 5):  # Loop from 1 to 4 (for 4 rows)
    for j in range(i, 0, -1):  # Loop backwards from 'i' to 1
        print(j, end="")  # Print the current value of 'j'
    print()  # Move to the next line after inner loop

"""
Problem: Reverse Triangle Pattern

Statement:
Given an integer n, create a reverse triangle pattern where:

- Each row i contains numbers from i down to 1 in descending order
- The pattern forms a right-aligned triangle
- Numbers decrease from left to right in each row
- The goal is to print the reverse triangle pattern

Return the printed pattern in the console.

Example for n=4:
1
21
321
4321
"""

from typing import List

class Solution:
    def reverseTriangle(self, n: int) -> List[str]:
        """
        Generate reverse triangle pattern with descending numbers.
        
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
            for j in range(i, 0, -1):
                row += str(j)
            result.append(row)
        
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    output = sol.reverseTriangle(4)
    for row in output:
        print(row)
