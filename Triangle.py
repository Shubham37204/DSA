# *****
# ****
# ***
# **
# *
for i in range(5):  
    for j in range(i,5):  
        print("*",end="")  
    print()


# *
# **
# ***
# ****
# *****
for i in range(5):  
    for j in range(i+1):  
        print("*",end="")  
    print()

"""
Problem: Triangle Pattern with Asterisks

Statement:
Given an integer n, create triangle patterns:

Pattern 1 - Inverted Triangle:
- Each row i contains (n-i) asterisks
- The pattern forms a right-aligned inverted triangle
- Asterisks decrease from top to bottom

Pattern 2 - Ascending Triangle:
- Each row i contains (i+1) asterisks
- The pattern forms a left-aligned triangle
- Asterisks increase from top to bottom

Return the printed patterns in the console.

Example for n=5:
Pattern 1:
*****
****
***
**
*

Pattern 2:
*
**
***
****
*****
"""

from typing import List

class Solution:
    def invertedAsteriskTriangle(self, n: int) -> List[str]:
        """
        Generate inverted triangle with asterisks.
        
        Args:
            n: Number of rows
            
        Returns:
            List of strings representing each row
            
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        result = []
        
        for i in range(n):
            row = "*" * (n - i)
            result.append(row)
        
        return result
    
    def ascendingAsteriskTriangle(self, n: int) -> List[str]:
        """
        Generate ascending triangle with asterisks.
        
        Args:
            n: Number of rows
            
        Returns:
            List of strings representing each row
            
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        result = []
        
        for i in range(n):
            row = "*" * (i + 1)
            result.append(row)
        
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print("Pattern 1 - Inverted:")
    output1 = sol.invertedAsteriskTriangle(5)
    for row in output1:
        print(row)
    
    print("\nPattern 2 - Ascending:")
    output2 = sol.ascendingAsteriskTriangle(5)
    for row in output2:
        print(row)