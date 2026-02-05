# arr = [5,4,3,2,1]
arr = [10, 20, 30, 40]
n = len(arr)

# Using different methods to reverse an array
# using built-in reverse method
# print(arr[::-1])
# arr.reverse()

# using for loop
print("using for loop to reverse the array")
for i in range(n // 2):
    arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
print(arr)

# using while loop
print("using while loop to reverse the array")
start = 0
end = len(arr) - 1

while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print("Reversed array:", arr)
