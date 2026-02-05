#Problem Statement: Given a string, write a program to Capitalize the first and last character of each word of that string.

class Solution:
    def Capital(self, s: str) -> str:
        words = s.split()
        result = []

        for word in words:
            if len(word) == 1:
                result.append(word.upper())
            else:
                capitalized = word[0].upper() + word[1:-1] + word[-1].upper()
                result.append(capitalized)

        return ' '.join(result)

sol = Solution()
print(sol.Capital("hello world from leetcode"))
