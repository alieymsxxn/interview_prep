from collections import  Counter


arr = [10, 20, 30, 40, 12, 10, 30, 100, 100, 100, 100, 100, 100]
k = 4
start, end = 0, 0
result = 0
buffer = Counter()

while end < len(arr):
    buffer.update([arr[end]])
    if len(buffer) < k:
        end += 1
    elif len(buffer) == k:
        result = max(result, (end - start + 1))
        end += 1
    elif len(buffer) > k:
        while len(buffer) > k:
            value = arr[start]
            buffer.update({value: -1})
            if buffer.get(value) == 0:
                del buffer[value]                 
            
            start += 1
        end += 1

pass