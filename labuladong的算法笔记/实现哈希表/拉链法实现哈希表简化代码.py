class KVNode:
    # 链表节点，存储 key-value 对儿
    def __init__(self, key, value):
        self.key = key
        self.value = value

class ExampleChainingHashMap:

    def __init__(self, capacity):
        # 底层 table 数组中的每个元素是一个链表
        self.table = [None] * capacity

    def hash(self, key):
        return key % len(self.table)

    def get(self, key):
        # 查
        index = self.hash(key)

        if self.table[index] is None:
            # 链表为空，说明 key 不存在
            return -1
        
        list = self.table[index]
        # 遍历链表，尝试查找目标 key ，返回对应的 value
        for node in list:
            if node.key == key:
                return node.value
            
        # 链表中没有目标 key
        return -1
    
    def put(self, key, value):
        # 增/改
        index = self.hash(key)

        if self.table[index] is None:
            # 链表为空，新建一个链表，插入 key-value
            self.table[index] = []
            self.table[index].append(KVNode(key, value))
            return
        
        list_ = self.table[index]
        for node in list_:
            if node.key == key:
                # key 已经存在，更新 value
                node.value = value
                return
            
        # 链表中没有目标 key，添加新节点
        # 这里使用 append 添加到链表尾部
        list_.append(KVNode(key, value))

    def remove(self, key):
        # 删
        list_ = self.table[self.hash(key)]
        if list_ is None:
            return
        
        # 如果 key 存在，则删除
        list_[:] = [node for node in list_ if node.key != key]