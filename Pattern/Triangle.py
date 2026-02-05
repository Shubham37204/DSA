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
"""

class Solution:
    def invertedAsteriskTriangle(self, n) :
        result = []
        
        for i in range(n):
            row = "*" * (n - i)
            result.append(row)
        
        return result
    
    def ascendingAsteriskTriangle(self, n):
        result = []
        
        for i in range(n):
            row = "*" * (i + 1)
            result.append(row)
        
        return result

