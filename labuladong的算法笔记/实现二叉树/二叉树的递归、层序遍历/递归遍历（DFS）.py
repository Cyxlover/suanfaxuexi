# 基本的二叉树节点
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# 二叉树的递归遍历框架
def traverse(root : TreeNode):
    if root is None:
        return
    # 前序遍历
    traverse(root.left)
    # 中序遍历
    traverse(root.right)
    # 后序遍历