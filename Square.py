# x=5;
# for i in range(1,x):
#     for j in range(i,x):
#         print(j , end = "")

#     print()
    
x=5;
# for i in range(1,x):
#     for j in range(1,x):
#         print(j , end = "")

#     print()


for i in range(1, x):
    ch = 'A'  # Initialize ch as 'A'
    for j in range(1, x):
        print(ch, end="")  # Print the current character
        ch = chr(ord(ch) + 1)  # Move to the next character in the alphabet
    print()  # Move to the next line after inner loop

"""
Problem: Square Pattern with Characters

Statement:
Given an integer n, create a square pattern of size (n-1) × (n-1) where:

- Each row contains consecutive alphabetic characters starting from 'A'
- Characters increment across each row
- Each row resets to 'A' and continues incrementing
- The goal is to print the square pattern with alphabetic characters

Return the printed pattern in the console.

Example for n=5:
ABCD
ABCD
ABCD
ABCD
"""

from typing import List

class Solution:
    def squareWithCharacters(self, n: int) -> List[str]:
        """
        Generate square pattern with consecutive characters.
        
        Args:
            n: Dimension of square
            
        Returns:
            List of strings representing each row
            
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        result = []
        
        for i in range(1, n):
            row = ""
            ch = 'A'
            for j in range(1, n):
                row += ch
                ch = chr(ord(ch) + 1)
            result.append(row)
        
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    output = sol.squareWithCharacters(5)
    for row in output:
        print(row)


