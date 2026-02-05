"""
Problem: Inverted Triangle Pattern

Statement:
Given an integer n, create an inverted triangle pattern where:

- Each row i is indented by i spaces
- Each row i contains (n-i) repeated digits/characters
- The pattern forms a right-aligned inverted triangle
- The goal is to print the inverted triangle pattern

Return the printed pattern in the console.

"""

class Solution:
    def invertedTriangle(self, n):

        result = []
        
        for i in range(1, n):
            row = " " * i + str(i) * (n - i)
            result.append(row)
        
        return result

