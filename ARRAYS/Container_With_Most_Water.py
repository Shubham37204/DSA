class Solution:
    def maxArea(self, height):
        ans = 0
        start ,end = 0, len(height) - 1

        while start < end:
            w = min(height[start], height[end])  # height of container
            width = end - start                  # width of container
            area = w * width                     # area
            ans = max(ans, area)

            # move the pointer at the shorter line
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return ans

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
