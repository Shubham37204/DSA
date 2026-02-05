class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        n = len(s)

        for i in range(n):
            if s[i] == '[' or s[i] == '{' or s[i] == '(':
                st.append(s[i])
            else:
                if len(st) == 0:      # stack is empty
                    return False
                if (st[-1] == '(' and s[i] == ')') or \
                   (st[-1] == '[' and s[i] == ']') or \
                   (st[-1] == '{' and s[i] == '}'):
                    st.pop()          # must call pop()
                else:
                    return False

        return len(st) == 0           # True if stack empty

s = Solution()                  # create object
print(s.isValid("([])"))        # call method on object

# The backslash \ is used as a line continuation character.
# It tells Python: “this line continues on the next line.”