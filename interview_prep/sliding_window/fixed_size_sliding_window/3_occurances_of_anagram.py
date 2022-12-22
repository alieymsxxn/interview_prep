from collections import Counter

text = 'fromffsffffromorff'
word = Counter('ffrom')
window = sum(word.values())

start, end = 0, 0
anagrams = []
temp = ''
count = 0

while end < len(text):
    char = text[end]
    if char in word:
        temp += char
    if (end - start) + 1 < window:
        end += 1
        
    elif (end - start) + 1 == window:
        if len(temp) == window: 
            if Counter(temp[-window:]) == word:
                anagrams.append(temp[-window:])
                count += 1
        if text[start] == temp[0]:
            temp = temp[1:]

        end += 1
        start += 1

pass