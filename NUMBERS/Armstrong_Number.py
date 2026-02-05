class Solution:
    def isArmstrong(self, s):
        # Explanation: 153 is a 3-digit number, and 1^3 + 5^3 + 3^3 = 153.
        u = s
        total = 0

        while u > 0:
            z = u % 10      # extract last digit
            y = z ** 3      # raise to power 3
            total += y
            u = u // 10     # remove last digit

        return total == s


print(Solution().isArmstrong(153))
