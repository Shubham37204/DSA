a = [2, 5, 1, 3, 0]
n = len(a)

# a.sort()
# print(a[1])
# print(a[n-2])

# It creates a positive infinity value.
smallest = second_smallest = float('inf')
# It creates a negative infinity value.
largest = second_largest = float('-inf')

for i in a:
    if i < smallest:
        second_smallest = smallest
        smallest = i
    elif i < second_smallest and i != smallest:
        second_smallest = i

    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print("Second smallest:", second_smallest)
print("Second largest:", second_largest)
