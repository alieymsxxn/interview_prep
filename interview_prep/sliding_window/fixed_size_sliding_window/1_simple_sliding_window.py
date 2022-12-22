# Given an array arr, find the sub-array of a particular size(window) with the largest sum 
arr = [1, 1, 3, 10, 1, 2, 11, 11, 11, 122, 12]
window = 2
i, j, output, ongoing_sum = 0, 0, 0, 0

while(j < len(arr)):
    ongoing_sum += arr[j]
    if (j - i + 1) != window:
        j += 1
    elif (j - i + 1) == window:
        output = max(output, ongoing_sum)
        ongoing_sum -= arr[i]
        i += 1
        j += 1

pass