from collections import deque

# 多叉树的层序遍历
# 每个节点自行维护 State 类，记录深度等信息
class State:
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth

    def levelOrderTraverse(root):
        if root is None:
            return
        q = deque()
        # 记录当前遍历到的层数（根节点视为第 1 层）
        q.append(State(root, 1))

        while q:
            state = q.popleft()
            cur = state.node
            depth = state.depth
            # 访问 cur 节点，同时知道它所在的层数
            print(f"depth = {depth}, val = {cur.val}")

            for child in cur.children:
                q.append(State(child, depth + 1))
        