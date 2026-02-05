def Powerset(a, ans, i, allSubset):
    if i == len(a):
        allSubset.append(ans.copy())  
        return

    ans.append(a[i])
    Powerset(a, ans, i + 1, allSubset)
    ans.pop()
    Powerset(a, ans, i + 1, allSubset)

arr = [1, 2, 3]
ans = []
allSubset = []
Powerset(arr, ans, 0, allSubset)
print(allSubset)
