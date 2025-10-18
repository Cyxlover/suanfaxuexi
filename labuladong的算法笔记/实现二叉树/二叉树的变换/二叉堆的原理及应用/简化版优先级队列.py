class SimpleMinPQ:
    # 底层使用数组实现二叉堆
    def __init__(self, capacity):
        # 初始化堆数组和大小
        self.heap = [0] * capacity
        self.size = 0

    # 父节点的索引
    def parent(self, node):
        return (node - 1) // 2
    
    # 左子节点的索引
    def left(self, node):
        return node * 2 + 1
    
    # 右子节点的索引
    def right(self, node):
        return node * 2 + 2
    
    # 交换数组的两个元素
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # 查，返回堆顶元素，时间复杂度 O(1)
    def peek(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # 增，向堆中插入一个元素，时间复杂度 O(logN)
    def push(self, x):
        # 把新元素追加到最后
        self.heap[self.size] = x
        # 然后上浮到正确位置
        self.swim(self.size)
        self.size += 1

    # 删，删除堆顶元素，时间复杂度 O(logN)
    def pop(self):
        res = self.heap[0]
        # 把堆底元素放到堆顶
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        # 然后下沉到正确位置
        self.sink(0)
        return res
    
    # 上浮操作，时间复杂度是树高 O(logN)
    def swim(self, node):
        while node > 0 and self.heap[self.parent(node)] > self.heap[node]:
            self.swap(self.parent(node), node)
            node = self.parent(node)

    # 下沉操作，时间复杂度是树高 O(logN)
    def sink(self, node):
        while self.left(node) < self.size or self.right(node) < self.size:
            # 比较自己和左右子节点，看看谁最小
            min_node = node
            if self.left(node) < self.size and self.heap[self.left(node)] < self.heap[min_node]:
                min_node = self.left(node)
            if self.right(node) < self.size and self.heap[self.right(node)] < self.heap[min_node]:
                min_node = self.right(node)
            if min_node == node:
                break
            # 如果左右子节点中有比自己小的，就交换
            self.swap(node, min_node)
            node = min_node

if __name__ == "__main__":
    pq = SimpleMinPQ(5)
    pq.push(3)
    pq.push(2)
    pq.push(1)
    pq.push(5)
    pq.push(4)

    print(pq.pop())     # 1
    print(pq.pop())     # 2
    print(pq.pop())     # 3
    print(pq.pop())     # 4
    print(pq.pop())     # 5