# Your class
class Solution:
    def isPrime(self, n):
        #for numbers less than 1
        if n < 2:
            return False
        #for others numbers
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


# Testing
obj = Solution()

# Example cases
print(obj.isPrime(5))   # Expected True  -> 5 is prime
print(obj.isPrime(10))  # Expected False -> 10 is not prime

# More test cases
print(obj.isPrime(1))   # Expected False
print(obj.isPrime(2))   # Expected True
print(obj.isPrime(17))  # Expected True
print(obj.isPrime(18))  # Expected False
