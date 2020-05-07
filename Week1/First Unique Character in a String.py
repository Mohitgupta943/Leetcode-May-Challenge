# Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/
'''
In this problem we can use a dictionary to store the count of each char. And then iterate in the string and check the count of each char and if it is 
1 we found our ans just return that index.
If the loop complets and we don't found any char with count then return -1.

Complexity Analysis: O(len(string))
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in s:
            if i not in d:
                d[i]=0
            d[i]+=1
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1
