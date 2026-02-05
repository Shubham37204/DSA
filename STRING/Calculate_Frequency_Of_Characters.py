#Problem Statement: Given a string, calculate the frequency of characters in a string.

# Example 1:
# Input: 
# Output: a2 d1 e1 f1 k1 o1 r2 t1 u1 w1 
# Explanation: Count of every character of string is printed

str ='takeuforward'
freq = {}

for i in str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for i, count in freq.items():
    print(f"{i} occurs {count} time(s) in the array")