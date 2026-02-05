class Solution(object):
    def removeWhitespaces(self, s):
        return s.replace(" ", "")

# Example usage:
sol = Solution()
s = "Hello World!"
print(sol.removeWhitespaces(s))  # Output: "HelloWorld!"
