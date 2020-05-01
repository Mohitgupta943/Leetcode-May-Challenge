#Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316/
'''
In this question we need to minimize the number to API calls. We can use binary search for finding first version as it is similar to finding
key in the array. 
'''
class Solution:
    def firstBadVersion(self, n):
        return self.bs(0,n)

    def bs(self,s,e):
        if e==s:
            return e
        mid=s+ (e-s)//2
        cur=isBadVersion(mid)    
        if cur==True:
            return self.bs(s,mid)
        if cur==False:
            return self.bs(mid+1,e)
            
  
