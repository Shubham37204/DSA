# 1
# 22
# 333
# 4444

# for i in range(4):  
#     for j in range(i+1):  
#         print(i+1,end="")  
#     print()

#A 
#B B B 
#C C C C
#D D D D D

ch = 'A' 
for i in range(4):
    for j in range(4):
        print(chr((ord(ch)) + i ) , end="")  
    print()

"""
Problem: Character Triangle Pattern

Statement:
Given an integer n, create a triangle pattern where:

- Each row i contains n repeated characters
- Characters increment by their row index
- Row 0 prints 'A' n times, Row 1 prints 'B' n times, etc.
- The goal is to print the character triangle pattern

Return the printed pattern in the console.

Example for n=4:
AAAA
BBBB
CCCC
DDDD
"""

from typing import List

class Solution:
    def characterTriangle(self, n: int) -> List[str]:
        """
        Generate character triangle pattern.
        
        Args:
            n: Number of rows
            
        Returns:
            List of strings representing each row
            
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        result = []
        
        for i in range(n):
            ch = chr(ord('A') + i)
            row = ch * n
            result.append(row)
        
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    output = sol.characterTriangle(4)
    for row in output:
        print(row)  