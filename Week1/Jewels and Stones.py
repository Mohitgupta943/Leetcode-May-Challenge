#Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/
'''
-------------------QUICK EXPLANATION------------------------------------
lookup is a array and initially all values are -1, first iterate through J and update the values in lookup array at ASCII value of chars 
present in J.
Now run a loop for S and for each char in S check if **lookup[ASCII value of char]==1**, if yes then increment final answer by 1.
'''
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        lookup={}
        ans=0
        for i in J:
            if i not in lookup:
                lookup[i]=1
        for i in S:
            
            if i in lookup:
                ans+=1
        return ans
