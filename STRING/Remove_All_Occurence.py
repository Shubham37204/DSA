class Solution(object):
    def repeatingElement(self, s, part):
        while part in s:
            s = s.replace(part, "", 1)  # remove the *leftmost* occurrence only
        return s

# Example usage:
sol = Solution()
s = "daabcbaabcbc"
part = "abc"
print(sol.repeatingElement(s, part))  # Output: "dab"
