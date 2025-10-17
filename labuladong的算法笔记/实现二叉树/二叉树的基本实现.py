class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

# 你可以这样构建一棵二叉树：
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

# 构造出来的二叉树是这样的：
#       1
#      / \
#     2   3
#    /   / \
#   4  5   6