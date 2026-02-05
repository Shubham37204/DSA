class Solution:
    def twoSum(self, arr, target):
        arr.sort()
        st , last = 0, len(arr)-1
        #two pointer approach
        while(st < last):
            s = arr[st]+arr[last]
            if s == target:
                return arr[st] , arr[last]
            elif s >  target:
                last -= 1
            else:
                st += 1
        return -1,-1

print(Solution().twoSum([1,3,4,3,5], 7))

