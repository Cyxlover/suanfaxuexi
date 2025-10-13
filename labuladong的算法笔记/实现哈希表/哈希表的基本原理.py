# 哈希表伪码逻辑
class MyHashMap:

    def __init__(self):
        self.table = [None] * 1000

    # 增/改，复杂度 O(1)
    def put(self, key, value):
        index = self.hash(key)
        self.table[index] = value

    # 查，复杂度 O(1)
    def get(self, key):
        index = self.hash(key)
        return self.table[index]

    # 删，复杂度 O(1)
    def remove(self, key):
        index = self.hash(key)
        self.table[index] = None

    # 哈希函数，把 key 转化成 table 中的合法索引
    # 时间复杂度必须是 O(1)，才能保证上述方法的复杂度都是 O(1)
    def hash(self, key):
        # ...
        pass