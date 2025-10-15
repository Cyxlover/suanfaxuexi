class MyHashSet:
    def __init__(self):
        # 底层字典，用于存储集合元素
        self.map = {}

    def add(self, key):
        # 向哈希集合添加一个键值对，值用 True 占位
        self.map[key] = True

    def remove(self, key):
        # 从哈希表中移除键 key
        if key in self.map:
            del self.map[key]

    def contain(self, key):
        # 判断哈希集合中是否存在键 key
        return key in self.map
    
    def size(self):
        # 返回哈希集合中元素的数量
        return len(self.map)