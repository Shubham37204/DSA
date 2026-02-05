class Solution:
    def PreviousSmallerElement(self, arr: list[int]) -> list[int]:
        n = len(arr)
        ans = [-1] * n   
        s = []
        for i in range(n):   # right → left
            while len(s) > 0 and s[-1] >= arr[i]:
                s.pop()
            if len(s) == 0: 
                ans[i] = -1
            else:
                ans[i] = s[-1]
            s.append(arr[i])   # must be inside loop
        return ans

    