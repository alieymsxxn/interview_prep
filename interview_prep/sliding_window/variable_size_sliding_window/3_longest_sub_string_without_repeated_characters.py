# Longest substring with unique characters
from collections import Counter

text = 'pwwkewaxc'
size = len(text)
buffer = Counter()
result = 0
start, end  = 0, 0
while end < size:
    buffer.update([text[end]])
    # The first condition is not necessary for this one
    if len(buffer) == (end - start + 1):
        result = max(result, (end - start +1))
    elif len(buffer) < (end - start + 1):
        while len(buffer) < (end - start + 1):
            value_to_remove = text[start]
            buffer.update({value_to_remove: -1})
            if buffer.get(value_to_remove) == 0:
                del buffer[value_to_remove]
            start += 1
    end += 1
pass
