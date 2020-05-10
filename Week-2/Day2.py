# Name: Valid Perfect Square
# Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324/
'''
If square root of given no. is integer then given no. will be perfect square
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sq=sqrt(num)
        return True if int(sq)==sq else False
