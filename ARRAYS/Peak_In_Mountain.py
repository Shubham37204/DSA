class Solution:
    def peakIndexInMountainArray(self, arr):
        start, end = 0, len(arr) - 1
        while start <= end:   # use <= so we don’t miss the peak
            mid = start + (end - start) // 2

            # check if mid is peak
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                #return mid   # return index, not value
                return arr[mid]

            elif arr[mid-1] < arr[mid]:
                # increasing slope → move right
                start = mid + 1
            else:
                # decreasing slope → move left
                end = mid - 1
s = Solution()
print(s.peakIndexInMountainArray([0,2,4,6,5,3,1]))
