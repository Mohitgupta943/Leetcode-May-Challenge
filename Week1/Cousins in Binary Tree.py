#Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/
'''
To solve this I have considered 4 variables p1,p2,d1,d2.
p1=parent of node having value=x
d1= depth of node having value=x

p2=parent of node having value=y
d2= depth of node having value=y

Simply apply DFS and above 4 values. Now if the condition for nodes to be cousin gets satisfied-
(i.e. parentX!=parentY && depthX==depthY) then return true
else return false

Time Complexity: same as time complexity of DFS i.e O(V+E), V=no. of vertices, E=no. of edges
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    p1=0
    p2=0
    d1=0
    d2=0
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.p1=0
        self.p2=0
        self.d1=0
        self.d2=0
        self.dfs(root,x,y,0)
        #print(self.d1,self.p1,self.d2,self.p2)
        if self.d1==self.d2 and self.p1 !=self.p2:
            return True
        else:
            return False
    
    def dfs(self,root,x,y,d):
        if root is None:
            return
        if root.left is not None:
            if root.left.val==x:
                self.p1=root.val
                self.d1=d+1
            if root.left.val==y:
                self.p2=root.val
                self.d2=d+1
                
        if root.right is not None:
            if root.right.val==x:
                self.p1=root.val
                self.d1=d+1
            if root.right.val==y:
                self.p2=root.val
                self.d2=d+1
        self.dfs(root.left,x,y,d+1)
        self.dfs(root.right,x,y,d+1)
