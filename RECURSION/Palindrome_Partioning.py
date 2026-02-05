def ispalin(s):
    s1 = list(s)         
    s1.reverse()
    return s == ''.join(s1)
    # s = "aba"
    # s1 = list(s)     # ['a', 'b', 'a']
    # s1.reverse()     # ['a', 'b', 'a']
    # ''.join(s1)      # "aba"

def getAllParts(s, partitions, ans):
    if len(s) == 0:
        ans.append(partitions.copy())
        return
    for i in range(len(s)):
        part = s[0:i+1]                        
        if ispalin(part):                     
            partitions.append(part)           
            getAllParts(s[i+1:], partitions, ans)  
            partitions.pop()                  

ans = []
getAllParts("aab", [], ans)
print(ans)
