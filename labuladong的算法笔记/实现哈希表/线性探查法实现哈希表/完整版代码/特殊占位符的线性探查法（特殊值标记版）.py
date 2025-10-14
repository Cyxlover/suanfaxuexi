class MyLinearProbingHashMap2:

    class KVNode:
        def __init__(self, key, val):
            self.key = key
            self.val = val

    # 被删除的 KVNode 的占位符
    DUMMY = KVNode(None, None)

    # 默认的初始化容量
    INIT_CAP = 4

    def __init__(self, cap = INIT_CAP):
        # 真正存储键值对的 table 数组
        self.table = [None] * cap
        # HashMap 中的键值对个数
        self.size = 0

    # 增/改

    # 添加 key -> val 键值对
    # 如果键 key 已存在，则将值修改为 val
    def put(self, key, val):
        if key is None:
            raise ValueError("key is none")

        # 负载因子默认设为 0.75，超过则扩容
        if self.size >= len(self.table) * 0.75:
            self.resize(len(self.table) * 2)

        index = self.get_key_index(key)
        if index != -1:
            # key 已存在，修改对应的 val
            self.table[index].val = val
            return
        
        # key 不存在
        x = MyLinearProbingHashMap2.KVNode(key, val)
        # 在 table 中找一个空位或者占位符，插入
        index = self.hash(key)
        while self.table[index] is not None and self.table[index] != MyLinearProbingHashMap2.DUMMY:
            index = (index + 1) % len(self.table)
        self.table[index] = x
        self.size += 1

    # 删

    # 删除 key 和对应的 val，并返回 val
    # 若 key 不存在，则返回 None
    def remove(self, key):
        if key is None:
            raise ValueError("key is none")

        # 缩容
        if self.size < len(self.table) // 8:
            self.resize(len(self.table) // 2)

        index = self.get_key_index(key)
        if index == -1:
            # key 不存在，不需要 remove
            return
        
        # 开始 remove
        # 直接用占位符表示删除
        self.table[index] = MyLinearProbingHashMap2.DUMMY
        self.size -= 1

    # 查
    
    # 返回 key 对应的 val
    # 如果 key 不存在，则返回 None
    def get(self, key):
        if key is None:
            raise ValueError("key is none")

        index = self.get_key_index(key)
        if index == -1:
            return None
        
        return self.table[index].val
    
    def contains_key(self, key):
        return self.get_key_index(key) != -1
    
    def keys(self):
        keys_list = []
        for entry in self.table:
            if entry is not None and entry != MyLinearProbingHashMap2.DUMMY:
                keys_list.append(entry.key)
        return keys_list
    
    def size(self):
        return self.size
    
    # 对 key 进行线性探查，返回一个索引
    # 根据 keys[i] 是否为 None 判断是否找到对应的 key
    def get_key_index(self, key):
        step = 0
        index = self.hash(key)
        while self.table[index] is not None:
            step += 1
            if step >= len(self.table):
                # 这里可以触发一次 resize，把标记为删除的占位符清理掉
                self.resize(len(self.table))
                return -1
            
            entry = self.table[index]
            # 遇到占位符直接跳过
            if entry == MyLinearProbingHashMap2.DUMMY:
                continue
            if entry.key == key:
                return index
            
            index = (index + 1) % len(self.table)

        return -1
    
    # 哈希函数，将键映射到 table 的索引
    # [0, table.length - 1]
    def hash(self, key):
        return hash(key) % len(self.table)

    def resize(self, cap):
        new_map = MyLinearProbingHashMap2(cap)
        for entry in self.table:
            if entry is not None and entry != MyLinearProbingHashMap2.DUMMY:
                new_map.put(entry.key, entry.val)
        self.table = new_map.table

if __name__ == "__main__":
    map = MyLinearProbingHashMap2()
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