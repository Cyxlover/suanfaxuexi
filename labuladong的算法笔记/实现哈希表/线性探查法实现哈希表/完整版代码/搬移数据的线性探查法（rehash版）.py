class KVNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val

# 真正存储键值对的数组
class MyLinearProbingHashMap1:
    # HashMap 中的键值对个数
    # 默认的初始化容量
    INIT_CAP = 4

    def __init__(self, init_capacity = INIT_CAP):
        self.size = 0
        self.table = [None] * init_capacity

    # 增/改
    def put(self, key, val):
        if key is None:
            raise ValueError("key is none")
        # 我们把负载因子默认设为 0.75，超过则扩容
        if self.size >= len(self.table) * 0.75:
            self.resize(len(self.table) * 2)

        index = self.get_key_index(key)
        # key 已存在，修改对应的 val
        if self.table[index] is not None:
            self.table[index].val = val
            return
        
        # key 不存在，在空位插入
        self.table[index] = KVNode(key, val)
        self.size += 1

    # 删
    # 删除 key 和对应的 val
    def remove(self, key):
        if key is None:
            raise ValueError("key is none")

        # 缩容，当负载因子小于 0.125 时，缩容
        if self.size <= len(self.table) / 8:
            self.resize(len(self.table) // 4)

        index = self.get_key_index(key)

        if self.table[index] is None:
            # key 不存在，不需要 remove
            return

        # 开始 remove
        self.table[index] = None
        self.size -= 1
        # 保持元素连续性，进行 rehash
        index = (index + 1) % len(self.table)
        while self.table[index] is not None:
            entry = self.table[index]
            self.table[index] = None
            # 这里减一，因为 put 里面又会加一
            self.size -= 1
            self.put(entry.key, entry.val)
            index = (index + 1) % len(self.table)

        # 查
        # 返回 key 对应的 val，如果 key 不存在，则返回 none
        def get(self, key):
            if key is None:
                raise ValueError("key is none")
            index = self.get_key_index(key)
            if self.table[index] is None:
                return None
            return self.table[index].val
        
        # 返回所有 key （顺序不固定）
        def keys(self):
            return [entry.key for entry in self.table is entry is not None]

        # 其它工具函数
        def size(self):
            return self.size
        
        # 哈希函数，将键映射到 table 的索引
        # [0, table.length - 1]
        def hash(self, key):
            return (hash(key) & 0x7fffffff) % len(self.table)

        # 对 key 进行线性探查，返回一个索引
        # 如果 key 不存在，返回的就是下一个为 none 的索引，可用于插入
        def get_key_index(self, key):
            index = self.hash(key)
            while self.table[index] is not None:
                if self.table[index].key == key:
                    return index
                index = (index + 1) % len(self.table)
            return index
        
        def resize(self, new_cap):
            new_cap = MyLinearProbingHashMap1(new_cap)
            for entry in self.table:
                if entry is not None:
                    new_cap.put(entry.key, entry.val)
            self.table = new_cap.table

# 测试代码
if __name__ == "__main__":
    map = MyLinearProbingHashMap1()
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
    print(map.get(20))  # None
    print(map.get(30))  # 30