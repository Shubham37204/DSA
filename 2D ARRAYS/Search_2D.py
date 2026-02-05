def SearchRow(a, t, r):
    n = len(a[0])
    st = 0
    end = n - 1
    while st <= end:
        mid = (st + end) // 2
        if t == a[r][mid]:
            return True
        elif t > a[r][mid]:
            st = mid + 1
        else:
            end = mid - 1
    return False

def SearchMatrix(a, t):
    row = len(a)
    col = len(a[0])
    start = 0
    end = row - 1
    while start <= end:
        mid = (start + end) // 2
        if t >= a[mid][0] and t <= a[mid][col - 1]:
            return SearchRow(a, t, mid)
        elif t > a[mid][col - 1]:
            start = mid + 1
        else:
            end = mid - 1
    return False

# Test
arr = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 34
print(SearchMatrix(arr, target))  # Output: True
