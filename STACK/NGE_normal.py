class Solution:
    def nextGreaterElement(self, arr):
        n = len(arr)
        ans = [-1] * n   # pre-fill with -1 it is beacuse ans[i] = -1
        s = []
        for i in range(n-1, -1, -1):   # right → left
            while len(s) > 0 and s[-1] <= arr[i]:
                s.pop()
            if len(s) == 0: 
                ans[i] = -1
            else:
                ans[i] = s[-1]
            s.append(arr[i])   # must be inside loop
        return ans


# Step-by-step dry run (for [4, 5, 2, 25])

# Start from rightmost element:

# i = 3 → arr[3] = 25

# stack = [] → nothing greater

# ans[3] = -1

# push 25 → stack = [25]

# i = 2 → arr[2] = 2

# stack top = 25 (> 2) → next greater = 25

# ans[2] = 25

# push 2 → stack = [25, 2]

# i = 1 → arr[1] = 5

# stack = [25, 2], pop 2 (≤ 5)

# stack top = 25 (> 5) → next greater = 25

# ans[1] = 25

# push 5 → stack = [25, 5]

# i = 0 → arr[0] = 4

# stack top = 5 (> 4) → next greater = 5

# ans[0] = 5

# push 4 → stack = [25, 5, 4]