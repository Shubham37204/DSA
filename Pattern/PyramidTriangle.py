"""
Problem: Pyramid Triangle Pattern

Statement:
Given an integer n, create a pyramid triangle pattern where:

- Each row i contains numbers from 1 to i, then back down from i-1 to 1
- The pattern forms a symmetrical pyramid
- Numbers increase towards the middle and then decrease
- The goal is to print the pyramid triangle pattern

Return the printed pattern in the console.
"""

class Solution:
    def pyramidTriangle(self, n):
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

