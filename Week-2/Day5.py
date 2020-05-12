
# Problem Name: Single Element in a Sorted Array
# Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3327/

'''
****Explanation******
Since, given in question that every element appears exactly twice, except for one element which appears exactly once. 
As we know that XOR of a element with itsel results in 0. EX. 5^5=0

We can use this property and xor all the elements of the array. All elements having twice occurance will result in zero and at last we 
will get the element which has single occurance.

For ex.
array=[1,1,2,3,3,4,4,8,8]
perform XOR= (1^1)^2^(3^3)^(4^4)^(8^8)==>2

Time Complexity: O(n)
Space Complexity: O(1) as we use one variable to store Xor of the array.

'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans=nums[0]
        for i in range(1,len(nums)):
            ans^=nums[i]
        return ans
