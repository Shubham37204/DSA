# 123
# 456
# 789
num = 1  
for i in range(3):  
    for j in range(3):  
        print(num, end="") 
        num += 1  
    print() 
     
#A B C
#D E F
#G H I
ch = 'A' 
for i in range(3):
    for j in range(3):
        print(ch, end="")  
        ch = chr(ord(ch) + 1) 
    print()

"""
Problem: Sequential Square Pattern

Statement:
Given an integer n, create a square pattern of size n × n where:

- Each cell contains consecutive numbers or consecutive alphabetic characters
- Numbers/characters increment sequentially across the entire square
- The pattern fills row by row from left to right
- The goal is to print the sequential square pattern

Return the printed pattern in the console.

Example for numbers (n=3):
123
456
789

Example for characters (n=3):
ABC
DEF
GHI
"""

from typing import List

class Solution:
    def sequentialSquareNumbers(self, n: int) -> List[str]:
        """
        Generate sequential square pattern with numbers.
        
        Args:
            n: Dimension of square
            
        Returns:
            List of strings representing each row
            
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        result = []
        num = 1
        
        for i in range(n):
            row = ""
            for j in range(n):
                row += str(num)
                num += 1
            result.append(row)
        
        return result
    
    def sequentialSquareCharacters(self, n: int) -> List[str]:
        """
        Generate sequential square pattern with characters.
        
        Args:
            n: Dimension of square
            
        Returns:
            List of strings representing each row
            
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        result = []
        ch = 'A'
        
        for i in range(n):
            row = ""
            for j in range(n):
                row += ch
                ch = chr(ord(ch) + 1)
            result.append(row)
        
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print("Numbers:")
    output1 = sol.sequentialSquareNumbers(3)
    for row in output1:
        print(row)
    
    print("\nCharacters:")
    output2 = sol.sequentialSquareCharacters(3)
    for row in output2:
        print(row)  