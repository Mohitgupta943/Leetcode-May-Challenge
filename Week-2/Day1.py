# Name= Check If It Is a Straight Line
#Problem Link :https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323/
'''
We have to check, if all given points lie on the straight line or not. To check that we can simly check if slope between consecutive pairs of 
points is same or not.

Equal slope between consecutive pair of points ensure that those points lie on a straight line.

Formula for Slope: (y2-y1)/(x2-x1). where (x1,y1) and (x2,y2) represent two points on the cartesian plane.

SPECIAL CASE: Carfully handel the case when slope is=1 i.e 90 degree and in that case x1==x2.

Time Complexity= O(len(array))
'''

class Solution:
    def checkStraightLine(self, a: List[List[int]]) -> bool:
        s=0
        if (a[1][0]==a[0][0]):
            s=10**9
        else:
            s=abs(a[1][1]-a[0][1])/abs(a[1][0]-a[0][0])
        ts=0
        for i in range(2,len(a)):
            if a[i][0]==a[i-1][0]:
                ts=10**9
            else:
                ts=abs(a[i][1]-a[i-1][1])/abs(a[i][0]-a[i-1][0])
            if ts!=s:
                return False
        return True
