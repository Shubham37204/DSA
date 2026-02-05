class Solution:
    def primeNumbersInRange(self, low, high):
        temp=[]
        for i in range(low,high+1):
            if i<2:
                return False
            for j in range(2,i):   
                if i%j==0:
                    break
                else:
                    temp.append(i)
        return temp

