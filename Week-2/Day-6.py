Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3328/
Problem Name: Remove K Digits                          Tag=Medium

******Quick Explanation*****
In this problem we have to remove K digits from given number such that the resultant number is smallest possible. To achieve this we have to
focus on two things:
1--> As we go from right to left the value of digit increases, this implies the we should focus on removing numbers from left.
  Ex= n=432,k=1 ==> remove 4 and we get 32 which is samllest possible.

2--> Conside n=243 and k=1.
      In this case we can not simply remove leftmost digit. As:
        If we remove 2 ====> 43
        If we remove 4 ====> 23
        If we remove 3 ====> 24
        
    OBSERVATION: Start from left and iterate while a[i]<a[i+1]. Also, be carefull, as after removing the digit if we are left with
                 leading zeros we need to remove them too. For--> 200013, after removing we are left with 00013.So we need to remove 
                 leading zeros.
                 
******Complexity Analysis****

1. Time Complexity: O(len(num))
2. Space Complexity: O(len(num))

******************************************  Code  **************************************************************************************
1. Iterative Solution:

class Solution:
    def removeKdigits(self, n: str, k: int) -> str:
        num=[i for i in n] #converting string to array of chars
        while k>0:
            if len(num)<=1:
                return "0"
            i=0
            while i<len(num)-1:
                if num[i]<=num[i+1]:
                    i+=1
                else:
                    break
            num.pop(i)
            while len(num)>1 and num[0]=='0': # Removing leading zeros
                num.pop(0)
            k-=1
        return "".join(num)
        
2. Recusrsive Solution:

  class Solution:
    def removeKdigits(self, n: str, K: int) -> str:
        num=[i for i in n]
       
        num=self.solve(num,K)
       
        i=0
        while len(num)>1 and num[i]=='0':
            num.pop(0)
        return "".join(num)
    
    def solve(self,num,k):
        
        if len(num)==1 and k>0:
            return ['0']
        if k==0:

            return num
        i=0
        while i<len(num)-1:
            if num[i]<=num[i+1]:
                i+=1
            else:
                break
        num.pop(i)

        return self.solve(num,k-1)
