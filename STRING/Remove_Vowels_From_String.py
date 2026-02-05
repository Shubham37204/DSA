def RemoveVowels(s):
    temp = []
    for i in range(len(s)):
        if s[i] in ('a', 'e', 'i', 'o', 'u'):
            continue
        else:
            temp.append(s[i])
    return ''.join(temp)  # add return and join the characters into a string

str = 'take u forward'
print(RemoveVowels(str))
