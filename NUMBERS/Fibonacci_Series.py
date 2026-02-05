class Solution:
    def fibonacciSeries(self, n):
        a, b = 0, 1
        for i in range(n):
            print(a, end=" ")
            c = a + b
            a = b
            b = c

Solution().fibonacciSeries(5)
