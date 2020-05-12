
#Problem Name:  Flood Fill
#Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3326/

'''
******Quick Explanation************
This question can be easily solved with the help of recursion and proper handeling of corner/base cases. In following code snipet 
"fill()" function is the recursive function.This function checks if the current index of the pixel (i,j) is within the range and also 
ensure if the color of current pixel is same as starting pixel. 

If all the above conditions get satisfied and if the current pixel has not been updated/visited, then we update it and recursively call fill
function for it neighbour pixels.
if (i,j) is current pixel, then neighbour pixels are:
up -->(i+1,j), down --> (i-1,j), right --> (i,j+1), left--> (i,j-1)

****Complexity Analysis:****
time complexity: O(n) as we are pruning visited/updated pixels
Space complexity: O(n)--> internal stack is used by recursive calls.

'''

class Solution:
    R=0
    C=0
    sp=0
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.R=len(image)    #Row length
        self.C=len(image[0]) #Column length
        self.sp=image[sr][sc] #sp is global variable representing starting pixel color
        self.fill(image,sr,sc,newColor)
        return image
    
    def fill(self,a,i,j,nc): # a->image, i,j->indices, nc->new color
       
        if i>=self.R or i<0:
            return
        if j>=self.C or j<0:
            return 
        if a[i][j]!=self.sp: 
            return
        # Removing below if statement will result in infinite loop, remove it and check it.
        if a[i][j]==nc: #if current pixel already updated then skip it
            return 
            
        a[i][j]=nc # if all conditons satisfy then update current pixe
        #recursive call for neighbouring pixels
        self.fill(a,i+1,j,nc)
        self.fill(a,i-1,j,nc)
        self.fill(a,i,j+1,nc)
        self.fill(a,i,j-1,nc)
        return
