class Solution:
    def gcd(self, a,b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)
