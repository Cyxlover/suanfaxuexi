class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

# 用线性探查法解决哈希冲突的简化实现（rehash版）
class ExampleLinearProbingHashMap1:
    def __init__(self, cap):
        # 哈希表的底层数组，每个索引存储一个键值对
        self.table = [None] * cap

    # 增/改
    def put(self, key, value):
        index = self.findKeyIndex(key)
        self.table[index] = Node(key, value)

    # 查，找不到就返回-1
    def get(self, key):
        index = self.findKeyIndex(key)
        return -1 if self.table[index] is None else self.table[index].val
    
    # 删
    def remove(self, key):
        index = self.findKeyIndex(key)
        if self.table[index] is None:
            return
        self.table[index] = None
        # 保持元素连续性，搬移数据（这个过程称为 rehash）
        index = (index + 1) % len(self.table)
        while self.table[index] is not None:
            entry = self.table[index]
            self.table[index] = None
            # 这个操作是关键，利用 put 方法，将键值对重新插入
            # 这样就能把它们移动到正确的 table 索引位置
            self.put(entry.key, entry.val)
            index = (index + 1) % len(self.table)

    # 线性探查表查找 key 在 table 中的索引
    # 如果找不到，返回的就是下一个为 null 的索引，可用于插入
    def findKeyIndex(self, key):
        index = self.hash(key)
        while self.table[index] is not None:
            if self.table[index].key == key:
                return index
            # 注意环形数组特性
            index = (index + 1) % len(self.table)
        return index
    
    def hash(self, key):
        return key % len(self.table)

if __name__ == "__main__":
    map1 = ExampleLinearProbingHashMap1(10)
    map1.put(1, 1)
    map1.put(2, 2)
    map1.put(10, 10)
    map1.put(20, 20)
    map1.put(30, 30)
    print(map1.get(1))  # 1
    print(map1.get(2))  # 2
    print(map1.get(20)) # 20

    map1.put(1, 100)
    print(map1.get(1))  # 100

    map1.remove(20)
    print(map1.get(20)) # -1
    print(map1.get(30)) # 30