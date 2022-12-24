# I found this one a bit challenging, particularly it's calculation part.
# In the problem we need to separate out the largest number in all the sub-arrays.

arr = [99991, 5, 18787878, 10, 50, 70, 73, -1, 993, 5980]
window_size = 5
end, start = 0, 0
buffer = []
result = []

while end < len(arr):
    if not buffer:
        buffer.append(arr[end])
    else:
        if buffer[0] < arr[end]:
            buffer.clear()
            remaining_window = window_size - (end - start + 1)
            if not remaining_window:
                buffer.append(arr[end])
            else:
                buffer.extend(arr[end: end + remaining_window + 1])
    if end - start + 1 < window_size:
        end += 1
    elif end - start + 1 == window_size:
        largest = buffer[0]
        result.append(largest)
        if arr[start] == largest:
            buffer.pop(0)
        start += 1
        end += 1

pass