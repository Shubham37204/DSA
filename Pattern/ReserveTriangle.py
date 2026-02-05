"""
Problem: Reverse Triangle Pattern

Statement:
Given an integer n, create a reverse triangle pattern where:

- Each row i contains numbers from i down to 1 in descending order
- The pattern forms a right-aligned triangle
- Numbers decrease from left to right in each row
- The goal is to print the reverse triangle pattern

Return the printed pattern in the console.
"""

class Solution:
    def reverseTriangle(self, n):
        result = []
        
        for i in range(1, n + 1):
            row = ""
            for j in range(i, 0, -1):
                row += str(j)
            result.append(row)
        
        return result
