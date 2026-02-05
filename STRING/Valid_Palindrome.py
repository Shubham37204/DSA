class Solution:
    def isAlpha(self, u: str) -> bool:
        # check if character is alphanumeric
        return ('0' <= u.lower() <= '9') or ('a' <= u.lower() <= 'z')

    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            if not self.isAlpha(s[start]):
                start += 1
                continue
            if not self.isAlpha(s[end]):
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True



sol = Solution()
s = "Ac3?e3c&aa"
print(sol.isPalindrome(s))
