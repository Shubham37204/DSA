# 1111
#  222
#   33
#    4
n=5
for i in range(1,n):

    for j in range(i):
        print(" ",end="")

    for j in range(0,n-i):
        print(i,end="")

    print()

# A A A A
#   B B B
#     C C 
#       D

"""
Problem: Inverted Triangle Pattern

Statement:
Given an integer n, create an inverted triangle pattern where:

- Each row i is indented by i spaces
- Each row i contains (n-i) repeated digits/characters
- The pattern forms a right-aligned inverted triangle
- The goal is to print the inverted triangle pattern

Return the printed pattern in the console.

Example for n=5:
1111
 222
  33
   4
"""

from typing import List

class Solution:
    def invertedTriangle(self, n: int) -> List[str]:
        """
        Generate inverted triangle pattern with spaces and repeated digits.
        
        Args:
            n: Number of rows
            
        Returns:
            List of strings representing each row
            
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        result = []
        
        for i in range(1, n):
            row = " " * i + str(i) * (n - i)
            result.append(row)
        
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    output = sol.invertedTriangle(5)
    for row in output:
        print(row)