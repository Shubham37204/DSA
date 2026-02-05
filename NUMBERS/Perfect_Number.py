class Solution:
    def checkPerfectNumber(self, num):
        # A perfect number must be greater than 1
        if num <= 1:
            return False
        
        # This will store the sum of divisors (excluding num itself)
        sum_of_divisors = 0

        # Check all numbers from 1 to num-1
        for i in range(1, num):
            if num % i == 0:  # If i divides num evenly, it's a divisor
                sum_of_divisors += i
        
        # If the sum of divisors equals the original number, it's perfect
        if sum_of_divisors == num:
            return True
        else:
            return False
