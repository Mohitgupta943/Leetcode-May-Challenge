Problem Link:https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/
'''
Quick Explanation:
********Some Background Knowledge needed for this question to be solved:********
When we represent a number in binary it is basically a string of 0's and 1's and each bit in binary string is associated/mutiplied with some 
power of two(2^x) and add them we get corresponding decimal number.
For Example:
Let say we have a binary string "101". To obtain corresponding decimal number we do:
(2^2)*1 + (2^1)*0 + (2^0) * 1=5 and we all know that numbers are stored in binary form in the memory. So we will use this Knowledge to solve this
problem.
The main idea to solve this question is to check the lowest significatn bit(LSB)---> if it is 0 then add the corresponding power of 2 to 
final ans else ignore.

COMPLEXITY ANALYSIS: O(log(num)) i.e the no. bits in the given number.

 Follow the code and read the comments to understand the code.
'''

class Solution:
    def findComplement(self, num: int) -> int:
        p=1
        ans=0
        if num==0: #if num is 0 simply return 1
            return 1
            
        while num>0:
            if num&1==0: # checking if Least significant bit is equal to 0
                ans+=p
            p*=2
            num>>=1  # right shift it is equivalent to num=num//2 and it pops out the LSB
        return ans
