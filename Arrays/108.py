# Definition for a binary tree node.
'''Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.'''
from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        total_nums=len(nums)
        if not total_nums:
            return None
        
        mid=total_nums//2
        return TreeNode(nums[mid],self.sortedArrayToBST(nums[:mid]),self.sortedArrayToBST(nums[mid+1 :]))

def inorderTraversal(node):
        result=[]
        if node:
            result.extend(inorderTraversal(node.left))
            result.append(node.val)
            result.extend(inorderTraversal(node.right))
        return result
        


if __name__ =='__main__':
    solution=Solution()
    nums=[-10,-3,0,5,10]
    root=solution.sortedArrayToBST(nums)
    result=inorderTraversal(root)
    print(result)
