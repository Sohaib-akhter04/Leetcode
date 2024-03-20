# Definition for a binary tree node.
from typing import List

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node,path,paths):
            if not node:
                return 
            path.append(str(node.val))
            if not node.right and not node.left:
                paths.append("->".join(path))
            else:
                dfs(node.left,path,paths)
                dfs(node.right,path,paths)
            path.pop()
        paths=[]
        dfs(root,[],paths)
        return paths


          
        



if __name__ == "__main__":
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.left=TreeNode(5)
    solution=Solution()
    print(solution.binaryTreePaths(root))
