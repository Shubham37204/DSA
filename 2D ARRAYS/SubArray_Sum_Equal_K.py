class Solution:
    def subarraySum(self, arr, k):
        n=len(arr)
        prefixSum=[0]*n
        count=0
        prefixSum[0] = arr[0]
        for i in range(1,n):
            prefixSum[i]=prefixSum[i-1]+arr[i]
        m = {}
        for j in range(n):
            if prefixSum[j] == k :
                count+=1
            val=prefixSum[j] - k
            if val in m:
                count+=m[val]
            if prefixSum[j] not in m:
                m[prefixSum[j]]= 0
            m[prefixSum[j]] +=1
        return count

print(Solution().subarraySum([9,4,0,20,3,10,5], 33))
