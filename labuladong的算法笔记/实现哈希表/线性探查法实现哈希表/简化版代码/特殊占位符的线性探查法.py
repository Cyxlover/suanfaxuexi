# 用线性探查法解决哈希冲突的简化实现（特殊占位符版）
class ExampleLinearProbingHashMap2:

    class KVNode:
        def __init__(self, key, val):
            self.key = key
            self.val = val

    # 用于标记被删元素的占位符
    DELETED = KVNode(-2, -2)

    # 真正存储键值对的数组
    def __init__(self, init_capacity):
        self.table = [None] * init_capacity

    # 增/改
    def put(self, key, val):
        index = self.find_key_index(key)
        if index != -1:
            node = self.table[index]
            if node is not None:
                node.val = val
                return
            
        # key 不存在
        node = self.KVNode(key, val)
        # 在 table 中找一个空位或者占位符进行插入
        index = self.hash(key)
        while self.table[index] is not None and self.table[index] != self.DELETED:
            index = (index + 1) % len(self.table)
        self.table[index] = node

    # 删
    def remove(self, key):
        index = self.find_key_index(key)
        if index == -1:
            # key 不存在，不需要 remove
            return
        # 直接用占位符表示删除
        self.table[index] = self.DELETED

    # 查，返回 key 对应的 val，如果 key 不存在，则返回 -1
    def get(self, key):
        index = self.find_key_index(key)
        if index == -1:
            return -1
        
        return self.table[index].val
    
    # 线性探查表查找 key 在 table 中的索引
    # 如果找不到，返回 -1
    def find_key_index(self, key):
        # 因为删除元素时只是标记为 DELETED，并不是真的删除，所以 table 可能会被填满，导致死循环
        # step 用来记录查找的步数，防止死循环
        step = 0
        index = self.hash(key)
        while self.table[index] is not None:
            step += 1
            # 防止死循环
            if step > len(self.table):
                return -1
            # 遇到占位符直接跳过
            if self.table[index] == self.DELETED:
                index = (index + 1) % len(self.table)
                continue
            if self.table[index].key == key:
                return index
            index = (index + 1) % len(self.table)
        
        return -1
    
    # 哈希函数，将键映射到 table 的索引
    def hash(self, key):
        return key % len(self.table)

if __name__ == "__main__":
    map = ExampleLinearProbingHashMap2(10)
    map.put(1, 1)
    map.put(2, 2)
    map.put(10, 10)
    map.put(20, 20)
    map.put(30, 30)
    map.put(3, 3)
    print(map.get(1))   # 1
    print(map.get(2))   # 2
    print(map.get(20))  # 20

    map.put(1, 100)
    print(map.get(1))   # 100

    map.remove(20)
    print(map.get(20))  # -1
    print(map.get(30))  # 30