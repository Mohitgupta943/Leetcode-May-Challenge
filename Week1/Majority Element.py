#Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/
'''
**************Quick Explanation**********

We have to find the majority element and by defination is "The majority element is the element that appears more than ⌊ n/2 ⌋ times."
Hear ⌊ n/2 ⌋ means floor(n/2).

********Approach 1 (HashMap(Dictionary)):*********************
	Simply create a dictionary (distinct elements as key and their count as value). Iterate over the given array and find count of 		each distinct elements. After that iterate in the dictionary and find the element whose count > floor(n/2).

	Example: nums=[1,2,3,3,5,3,3] -------> dictionary={1:1, 2:1, 3:4, 5:1} ======> element 3 have count greater than floor(n/2).

	Complexity Analysis: O(n)  but we have to use extra space for creating dictionary(Hashmap).

**********Approach 1 (Sorting without any extra space):**********

	On the basis of definititon of majority elements we can say more than half of elements of arrya will be the majority elements.
	So, if we sort the array then simply element at index=n/2(integer division) will be majority element. 
	
	Example: nums=[1,2,3,3,5,3,3] ----sort--->[1,2,3,3,3,3,5]=======> element at index=(7/3) i.e. nums[3]=3
	
	Complexity Analysis: O(nlog(n))  but we have not used any extraspace.

In both approaches we can see a tradeoff between space and time but in this question both approaches works fine.


'''
#Approach 2 solution:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       
        return nums[len(nums)//2]
