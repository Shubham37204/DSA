"""
Problem: Square Pattern with Characters

Statement:
Given an integer n, create a square pattern of size (n-1) × (n-1) where:

- Each row contains consecutive alphabetic characters starting from 'A'
- Characters increment across each row
- Each row resets to 'A' and continues incrementing
- The goal is to print the square pattern with alphabetic characters

Return the printed pattern in the console.
"""


class Solution:
    def squareWithCharacters(self, n):
        result = []

        for i in range(1, n):
            row = ""
            ch = 'A'
            for j in range(1, n):
                row += ch
                ch = chr(ord(ch) + 1)
            result.append(row)
        
        return result



