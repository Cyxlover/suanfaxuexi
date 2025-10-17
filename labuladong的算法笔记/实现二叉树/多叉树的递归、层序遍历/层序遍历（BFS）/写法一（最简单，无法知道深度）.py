from collections import deque

def level_order_traverse(root):
    if root is None:
        return
    
    q = deque()
    q.append(root)

    while q:
        cur = q.popleft()
        # 访问 cur 节点
        print(cur.val)

        # 把 cur 的所有子节点加入队列
        for child in cur.children:
            q.append(child)