def lengthOfLastWord(s: str) -> int:
    count = 0
    s = s.rstrip()
    pointer = len(s) - 1

    while pointer >= 0:
        if ' ' in s and s[pointer] != ' ':
            count += 1
            pointer -= 1
        elif ' ' not in s:
            return len(s)
        else:
            return count
    
s = "a"
d = "This flag"
print(lengthOfLastWord(s))
print(lengthOfLastWord(d))