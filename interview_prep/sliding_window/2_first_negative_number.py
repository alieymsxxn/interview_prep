# This is a bit improvised version of the algorithm that we saw in example one
# we can optimize it by getting the index of the first negative. We might be able to
# reuse the index because our windows are overlapping. So, if index of negative in
# first window is not 0, it would reappear in the second or maybe third window as well
# I've applied this improvisation and it works and has most certainly increased the efficiency!

sample = [1, -1, -10, 10, 21, -2, -3, -12, 13, 14, 5, -5]
window = 3

start, end, number, index = 0, 0, 0, -1
result = []

def find_first_negative(arr):
    for index, item in enumerate(arr):
        if item < 0:
            return index, item
    return -1, 0

end = window - 1 + start

while end < len(sample):
    if index < 0:
        index, number = find_first_negative(sample[start:end+1])
    
    result.append(number)
    start += 1
    end += 1
    index -= 1
    # if (end - start + 1) < window:
    #     end += 1
    # if (end - start + 1) == window:
        # index, number = find_first_negative(sample[start:end+1])
        # start += 1
        # end += 1

pass