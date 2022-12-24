from collections import  Counter


arr = [10, 20, 30, 40, 12, 10, 30, 100, 100, 100, 100, 100, 100]
k = 4
start, end = 0, 0
result = 0
buffer = []

while end < len(arr):
    buffer.append(arr[end])
    unique_count = len(Counter(buffer)) 
    if unique_count < k:
        end += 1
    elif unique_count == k:
        result = max(result, len(buffer))
        end += 1
    elif unique_count > k:
        while unique_count > k:
            buffer.remove(arr[start])
            unique_count = len(Counter(buffer)) 
            start += 1
        end += 1

pass