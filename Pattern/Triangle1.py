
"""
Problem: Character Triangle Pattern

Statement:
Given an integer n, create a triangle pattern where:

- Each row i contains n repeated characters
- Characters increment by their row index
- Row 0 prints 'A' n times, Row 1 prints 'B' n times, etc.
- The goal is to print the character triangle pattern

Return the printed pattern in the console.
"""
class Solution:
    def characterTriangle(self,n):
        result = []
        
        for i in range(n):
            ch = chr(ord('A') + i)
            row = ch * n
            result.append(row)
        
        return result

