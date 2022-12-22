# Given an array arr of positive number, find the size of longest sub-array 
# that is equal to k.
arr = [4, 1, 1, 1, 2, 3, 5]
k = 5
start, end, result, ongoing_sum = 0, 0, 0, 0

while(end < len(arr)):
    ongoing_sum += arr[end]
    if ongoing_sum < k:
        end += 1
    elif ongoing_sum == k:
        result = max(result, (end - start) + 1)
        end += 1
    elif ongoing_sum > k:
        while ongoing_sum > k:
            ongoing_sum -= arr[start]
            start += 1
        end += 1


pass