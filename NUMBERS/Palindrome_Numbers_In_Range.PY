class Solution:
    def palindromeNumbersInRange(self, low, high):
        temp = []
        for i in range(low, high + 1):
            u = str(i)
            if u[::-1] == u:
                temp.append(i)
            else:
                continue
        return temp
 