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
        result = max(result, sum(buffer.values()))
        end += 1
    elif len(buffer) > k:
        while len(buffer) > k:
            value = buffer[arr[start]]
            
            if (value - 1) == 0:
                del buffer[arr[start]] 
            else:
                buffer.update({arr[start]: -1})
            
            start += 1
        end += 1

pass