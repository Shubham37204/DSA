class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.strip().split()[::-1])
    
# Input:  "  hello   world  "
# Step 1: s.strip()        → "hello   world"
# Step 2: .split()         → ['hello', 'world']
# Step 3: [::-1]           → ['world', 'hello']
# Step 4: ' '.join(...)    → "world hello"
