# A kid goes to mall with his mom and asks her to buy him gifts from 
# the racks of gifts. His mom agrees to let him get on two conditions
# 1) Gifts should be picked in a continuous manner not randomly.
# 2) Only two types of gifts should be picked. Not more than two types. 
from collections import Counter

# chars represent types of gifts
toys = ['a', 'b', 'c', 'a', 'a', 'a', 'a', 'b', 'a', 'a', 'c', 'd'] 
k = 2
counter = Counter()
start, end = 0, 0
count = 0

while end < len(toys):
    counter.update([toys[end]])
    if len(counter) < k:
        end += 1
    elif len(counter) == k:
        count = max(count, (end - start + 1))
        end += 1
    elif len(counter) > k:
        while len(counter) > k: 
            toy_type_to_remove = toys[start]
            counter.update({toy_type_to_remove: -1})
            if counter.get(toy_type_to_remove) == 0:
                del counter[toy_type_to_remove]
            start += 1
        end += 1
        
pass