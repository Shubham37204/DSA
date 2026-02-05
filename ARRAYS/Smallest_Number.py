a = [2, 5, 1, 3, 0]

# a.sort()
# print(a)
# print(a[0])

n = len(a)
smallest = a[0]
for i in range(1, n):
    if a[i] < smallest:
        smallest = a[i]
print(smallest)
