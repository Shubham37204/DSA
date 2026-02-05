nums = [1, 2, 3, 4]
n = len(nums)

ls = []
for i in range(n):
    product = 1
    for j in range(n):
        if i != j:
            product *= nums[j]  
    ls.append(product)         
print(ls)  # Output: [24, 12, 8, 6]


#2 method
def productExceptSelf(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    output = [1] * n

    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    for i in range(n):
        output[i] = left[i] * right[i]

    return output

nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]
