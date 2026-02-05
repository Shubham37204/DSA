class Solution:
    def isPalindrome(self, x: int) -> bool:
        u = str(x)
        if u[::-1] == u:
            return True
        else: 
            return False
