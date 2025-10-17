# 二叉树的递归遍历框架
def traverse_binary_tree(root):
    if root is None:
        return
    # 前序遍历
    traverse_binary_tree(root.left)
    # 中序遍历
    traverse_binary_tree(root.right)
    # 后序遍历

# N 叉树的遍历框架
def traverse_n_ary_tree(root):
    if root is None:
        return
    # 前序遍历
    for child in root.children:
        traverse_n_ary_tree(child)
    # 后序遍历