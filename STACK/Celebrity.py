class Solution:
    def findCelebrity(self, arr: list[list[int]]) -> int:
        n = len(arr)
        stack = []

        # Step 1: Push everyone into stack
        for i in range(n):
            stack.append(i)

        # Step 2: Eliminate non-celebrities
        while len(stack) > 1:
            i = stack.pop()
            j = stack.pop()

            if arr[i][j] == 0:
                # i does not know j → j cannot be celebrity
                stack.append(i)
            else:
                # i knows j → i cannot be celebrity
                stack.append(j)

        # Step 3: Potential celebrity
        celeb = stack[-1]   

        # Step 4: Verify celebrity
        for i in range(n):
            if i != celeb and (arr[i][celeb] == 0 or arr[celeb][i] == 1):
                return -1

        return celeb

arr = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 1, 0]
]

sol = Solution()
print(sol.findCelebrity(arr))  # Output: 1
