class MyPriorityQueue:
    def __init__(self, capacity, comparator = None):
        # 堆数组
        self.heap = [None] * capacity

        # 堆中元素的数量
        self.size = 0

        # 元素比较器
        self.comparator = comparator if comparator is not None else lambda x, y: (x > y) - (x < y)
        
    # 返回堆的大小
    def size(self):
        return self.size
    
    # 判断堆是否为空
    def is_empty(self):
        return self.size == 0
    
    # 父节点的索引
    def parent(self, node):
        return (node - 1) // 2
    
    # 左子节点的索引
    def left(self, node):
        return node * 2 +1
    
    # 右子节点的索引
    def right(self, node):
        return node * 2 + 2
    
    # 交换数组的两个元素
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # 查，返回堆顶元素，时间复杂度 O(1)
    def peek(self):
        if self.is_empty():
            raise IndexError("Priority queue underflow")
        return self.heap[0]

    # 增，向堆中插入一个元素，时间复杂度 O(logN)
    def push(self, x):
        # 扩容
        if self.size == len(self.heap):
            self.resize(2 * len(self.heap))

        # 把新元素追加到最后
        self.heap[self.size] == x
        # 然后上浮到正确位置
        self.swim(self.size)
        self.size += 1

    # 删，删除堆顶元素，时间复杂度 O(logN)
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority queue underflow")

        res = self.heap[0]
        # 把堆底元素放到堆顶
        self.swap(0, self.size - 1)
        # 避免对象游离
        self.heap[self.size - 1] = None
        self.size -= 1

        # 然后下沉到正确位置
        self.sink(0)

        # 缩容
        if self.size > 0 and self.size == len(self.heap) // 4:
            self.resize(len(self.heap) // 2)

        return res
    
    # 上浮操作，时间复杂度是树高 O(logN)
    def swim(self, node):
        while node > 0 and self.comparator(self.heap[self.parent(node)], self.heap[node]) > 0:
            self.swap(self.parent(node), node)
            node = self.parent(node)

    # 下沉操作，时间复杂度是树高 O(logN)
    def sink(self, node):
        while self.left(node) < self.size:
            # 比较自己和左右子节点，看看谁最小
            min_node = node
            if self.left(node) < self.size and self.comparator(self.heap[self.left(node)], self.heap[min_node]) < 0:
                min_node = self.left(node)
            if self.right(node) < self.size and self.comparator(self.heap[self.right(node)], self.heap[min_node]) < 0:
                min_node = self.right(node)
            if min_node == node:
                break
            # 如果左右子节点中有比自己小的，就交换
            self.swap(node, min_node)
            node = min_node

    # 调整堆的大小
    def resize(self, capacity):
        assert capacity >= self.size
        new_heap = [None] * capacity
        for i in range(self.size):
            new_heap[i] = self.heap[i]
        self.heap = new_heap

# 测试代码
if __name__ == "__main__":
    # 小顶堆
    pq = MyPriorityQueue(3, comparator=lambda x, y: (x > y) - (x < y))
    pq.push(3)
    pq.push(1)
    pq.push(4)
    pq.push(1)
    pq.push(5)
    pq.push(9)

    # 1 1 3 4 5 9
    while not pq.is_empty():
        print(pq.pop())