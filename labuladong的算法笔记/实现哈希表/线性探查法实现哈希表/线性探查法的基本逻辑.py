# 线性探查法的基本逻辑，伪码实现

class KVNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MyLinearProbingHashMap:
    # 数组中每个元素都存储一个键值对
    def __init__(self):
        self.table = [None] * 10

    def hash(self, key):
        return key % len(self.table)

    def put(self, key, value):
        index = self.hash(key)
        node = self.table[index]
        if node is None:
            self.table[index] = KVNode(key, value)
        else:
            # 线性探查法的逻辑
            # 向后探查，直到找到 key 或者找到空位
            while index < len(self.table) and self.table[index] is not None and self.table[index].key != key:
                index += 1
            self.table[index] = KVNode(key, value)

    def get(self, key):
        index = self.hash(key)
        # 向后探查，直到找到 key 或者找到空位
        while index < len(self.table) and self.table[index] is not None and self.table[index].key != key:
            index += 1
        if self.table[index] is None:
            return -1
        return self.table[index].value
    
    def remove(self, key):
        index = self.hash(key)
        # 向后探查，知道找到 key 或者找到空位
        while index < len(self.table) and self.table[index] is not None and self.table[index].key != key:
            index += 1
        # 删除 table[index]
        # ...