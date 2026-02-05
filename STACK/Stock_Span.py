class Solution:
    def stockSpan(self, prices: list[int]) -> list[int]:
        n=len(prices)
        ans = [0]*n
        st=[]
        for i in range(n):
            while (len(st)> 0 and prices[st[-1]]<prices[i]):
                st.pop()
            if len(st) == 0:
                ans[i] = i+1
            else:
                ans[i] = i-st[-1]
            st.append(i)
        return ans
s = Solution()                  
print(s.stockSpan([100,80,60,70,60,75,85]))        
