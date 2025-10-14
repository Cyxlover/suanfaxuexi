class MyChainingHashMap:

    # 拉链法使用的单链表节点，存储 key-value 对
    class KVNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    # 哈希表的底层数组，每个数组元素是一个链表，链表中的每个节点是 KVNode 存储键值对
    def __init__(self, init_capacity=4):
        # 哈希表中存入的键值对个数
        self.size = 0
        # 保证底层数组的容量至少为 1，因为 hash 函数中有求余运算，避免出现除以 0 的情况
        self.capacity = max(init_capacity, 1)
        # 初始化哈希表
        self.table = [[] for _ in range(self.capacity)]

    # 增/改

    # 添加 key -> val 键值对
    # 如果键 key 已存在，则将值修改为 val
    def put(self, key, value):
        if key is None:
            raise ValueError("key is none")
        index = self._hash(key)
        bucket = self.table[index]
        # 如果 key 之前存在，则修改对应的 val
        for node in bucket:
            if node.key == key:
                node.value = value
                return
        # 如果 key 之前不存在，则插入，size 增加
        bucket.append(self.KVNode(key, value))
        self.size += 1

        # 如果元素数量超过了负载因子，进行扩容
        if self.size >= self.capacity * 0.75:
            self.__resize(self.capacity * 2)

    # 删
    
    # 删除 key 和对应的 val
    def remove(self, key):
        if key is None:
            raise ValueError("key is none")
        index = self._hash(key)
        bucket = self.table[index]
        # 如果 key 存在，则删除，size 减少
        for node in bucket:
            if node.key == key:
                bucket.remove(node)
                self.size -= 1

                # 缩容，当负载因子小于 0.125 时，缩容
                if self.size <= self.capacity / 8:
                    self._resize(max(self.capacity // 4, 1))
                return
            
    # 查

    # 返回 key 对应的 val，如果 key 不存在，则返回 none
    def get(self, key):
        if key is None:
            raise ValueError("key is none")
        index = self._hash(key)
        bucket = self.table[index]
        for node in bucket:
            if node.key == key:
                return node.value
        return None
    
    # 返回所有 key
    def keys(self):
        keys = []
        for bucket in self.table:
            for node in bucket:
                keys.append(node.key)
        return keys
    
    # 其他工具函数

    def size(self):
        return self.size
    
    # 哈希函数，将键映射到 table 的索引
    def _hash(self, key):
        return hash(key) % self.capacity
    
    def _resize(self, new_capacity):
        # 构建一个新的 HashMap
        new_map = MyChainingHashMap(new_capacity)
        # 穷举当前 HashMap 中的所有键值对
        for bucket in self.table:
            for node in bucket:
                # 将键值对转移到新的 HashMap 中
                new_map.put(node.key, node.value)
        # 将当前 HashMap 的底层 table 换掉
        self.table = new_map.table
        self.capacity = new_capacity

# 测试代码
if __name__ == "__main__":
    map = MyChainingHashMap()
    map.put(1, 1)
    map.put(2, 2)
    map.put(3, 3)
    print(map.get(1))   # 1
    print(map.get(2))   # 2

    map.put(1, 100)
    print(map.get(1))   # 100
     
    map.remove(2)
    print(map.get(2))   # None
    print(map.key())    # [1, 3]

    map.remove(1)
    map.remove(2)
    map.remove(3)
    print(map.get(1))   # None