class Solution:
    def stackOperations(self, nums: list[int]) -> list[int]:
        stack = []
        for x in nums:
            stack.append(x)   # push

        result = []
        while stack:
            result.append(stack.pop())  # collect popped order

        return result   # reversed order of nums
