class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    diameter = 0  # stores the maximum diameter calculated
    def depth(self, node: [TreeNode]) -> int:
        if node is None:
            return 0
        left = self.depth(node.left)
        print(f"left: {left} 返回節點：{node.val}")
        right = self.depth(node.right)
        print(f"right: {right} 返回節點：{node.val}")
        # Calculate diameter
        if left + right > self.diameter:
            self.diameter = left + right
            print("深度相加")
        # Make sure the parent node(s) get the correct depth from this node
        print(f"深度diameter為: {self.diameter} \n")
        return 1 + max(left, right)
         
    def diameterOfBinaryTree(self, root: [TreeNode]) -> int:
        self.depth(root)  # root is guaranteed to be a TreeNode object
        return self.diameter
        
    
tree1 = TreeNode(1)
tree1.left = TreeNode(2, TreeNode(4), TreeNode(5))
tree1.right = TreeNode(3)

solution = Solution()
result1 = solution.diameterOfBinaryTree(tree1)
print(result1)  # 3