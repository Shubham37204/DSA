# 1
# 121
# 12321
# 1234321

for i in range(5):
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1, 0, -1):  
        print(j, end="") 
    print()

"""
Problem: Pyramid Triangle Pattern

Statement:
Given an integer n, create a pyramid triangle pattern where:

- Each row i contains numbers from 1 to i, then back down from i-1 to 1
- The pattern forms a symmetrical pyramid
- Numbers increase towards the middle and then decrease
- The goal is to print the pyramid triangle pattern

Return the printed pattern in the console.

Example for n=4:
1
121
12321
1234321
"""

from typing import List

class Solution:
    def pyramidTriangle(self, n: int) -> List[str]:
        """
        Generate pyramid triangle pattern with ascending and descending numbers.
        
        Args:
            n: Number of rows
            
        Returns:
            List of strings representing each row
            
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        result = []
        
        for i in range(n):
            row = ""
            # Ascending part
            for j in range(1, i + 2):
                row += str(j)
            # Descending part
            for j in range(i, 0, -1):
                row += str(j)
            result.append(row)
        
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    output = sol.pyramidTriangle(4)
    for row in output:
        print(row)