"""
Problem: Incrementing Triangle Pattern

Statement:
Given an integer n, create a triangle pattern where:

- Each row i contains numbers from 1 to i
- The pattern forms a left-aligned triangle
- Numbers increase from 1 up to the row index for each row
- The goal is to print the incrementing triangle pattern

"""


class Solution:
    def incrementingTriangle(self, n):
        
        result = []
        
        for i in range(1, n + 1):
            row = ""
            for j in range(1, i + 1):
                row += str(j)
            result.append(row)
        
        return result

