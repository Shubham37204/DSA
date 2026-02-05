class Solution:
    def nextGreaterElement(self, arr):
        n = len(arr)
        ans = [-1] * n   # pre-fill with -1 it is beacuse ans[i] = -1
        s = []
        for i in range(2*n-1, -1, -1):   # right → left
            while len(s) > 0 and s[-1] <= arr[i%n]:
                s.pop()
            if len(s) == 0: 
                ans[i%n] = -1
            else:
                ans[i%n] = s[-1]
            s.append(arr[i%n])   # must be inside loop
        return ans


# We use 2*n because the array is circular. Looping twice ensures every element can "see" elements on both its right and left side.
# We use i % n because when looping up to 2*n, the index can go out of bounds.When we loop 2*n times, i can go up to 2*n-1.

#But arr has only n elements (indices 0 … n-1). i% n wraps it back into the valid range 0 … n-1, so answers stay within the original array size.
# 👉 In short:
# 2*n → We loop twice so every element gets a chance to look all the way around the circle.
# i % n → Since the loop goes beyond n, this wraps the index back into the valid range (0 … n-1).