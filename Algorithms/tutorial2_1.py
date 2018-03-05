"""
Design an algorithm to check whether two given words are anagrams,
that is, whether one can be obtained from the other by permuting its letters.
For example, garner and ranger are anagrams.
"""

dic = {}
for i in range(0, 25):
    dic[chr(ord('a') + i)] = 0

with open("Algorithms\input.txt", 'r+') as f:
    strarray = f.read().split()
    for ch in strarray[0]:
        dic[ch] += 1

    for ch in strarray[1]:
        dic[ch] -= 1

    for item in dic:
        if dic[item] != 0:
            f.write('No')
            break
    else:
        f.write('Yes')
