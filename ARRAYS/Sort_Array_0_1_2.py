#dutch national flag

class Solution:
    def sortColors(self, nums):
        n=len(nums)
        low,mid,high=0,0,n-1
        if(nums[nums]==0):
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif(nums[mid]==1):
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
        return nums
                
