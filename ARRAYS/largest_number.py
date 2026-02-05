a = [2, 5, 1, 3, 0]
n = len(a)

# a.sort()
# print(a[n-1])

largest = a[0]
for i in range(1, n):
    if a[i] > largest:
        largest = a[i]
print(largest)
