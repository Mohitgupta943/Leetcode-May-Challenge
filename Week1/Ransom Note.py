Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/
'''
Create an array of size(26) for storing count of characters appearing in magazines string.
iterate in magazines string and increment the corresponding characters count in buffer array.
iterate in ransomnotes string and decrement the corresponding characters count in buffer array.
if any char count become less than 0 it implies that that char's count in ransom notes is grater than that in magazines string.

Complexity Analysis: O(len(magazines)+len(ransomnotes))
'''

class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        buffer=[0 for i in range(26)]
        for i in m:
            buffer[ord(i)-97]+=1
        for i in r:
            buffer[ord(i)-97]-=1
            if buffer[ord(i)-97]<0:
                return False
        return True
