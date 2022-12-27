# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from collections import Counter 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        counter = Counter()
        start, end = 0, 0

        while end < len(s):
            counter.update([s[end]])
            if (end - start + 1) == len(counter):
                result = max(result, (end - start + 1))
            elif (end - start + 1) > len(counter):
                while (end - start + 1) > len(counter):
                    to_remove = s[start]
                    counter.update({to_remove: -1})
                    if counter.get(to_remove) == 0:
                        del counter[to_remove]
                    start += 1
            end += 1

        return result