class solution:
    def SpiralMatrix(self,s,m,n):
        srow=scol=0
        erow=m-1
        ecol=n-1

        for j in range(scol,ecol):
            s[srow][j]
        
        for i in range(srow+1,erow):
            s[i][ecol]
        
        for j in range(ecol-1,scol):
            s[erow][j]

        for i in range(erow-1,srow+1):
            s[i][scol]

        srow+=1
        scol+=1
        erow-=1
        ecol-=1
