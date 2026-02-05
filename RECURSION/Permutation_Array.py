def getPermutation(nums,ans,i):
    if i == len(nums):
        ans.append(nums.copy())
        return

    for j in range(i,len(nums)):
        nums[i],nums[j] =nums[j],nums[i]
        getPermutation(nums,ans,i+1)
        nums[i],nums[j] =nums[j],nums[i]

arr = [1,2,3]
ans =[]
getPermutation(arr,ans,0)
print(ans)
