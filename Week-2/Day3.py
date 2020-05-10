# Name  Find the Town Judge
# Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325/

'''
Given--> [firstperson,secondperson]

I maintained two dictionaries d and cn.
d: stores key as secondperson and value as count of person trusting him/her.
cn: stores key as firstperson and value as count of person trusting him/her.

Now for person to be judge following condition should be satisfied:
 d[judge] == (N-1) && cn[judge]==0,  where N= no. of person in city.
 
This solution can be improved but it works although extra space used here is more.

Time Complexity: O(N)
'''

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        d={}
        cn={}
        if N==1 and len(trust)==0:
            return N
        for i in trust:
            b=i[1]
            x=i[0]
            if b not in d:
                d[b]=0
            if x not in cn:
                cn[x]=0
            if b not in cn:
                cn[b]=0
            d[b]+=1
            cn[x]+=1
       
        for i in d:
            if d[i]==N-1:
                if cn[i]==0:
                    return i
        return -1
