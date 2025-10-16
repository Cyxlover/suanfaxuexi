class MyLinkedHashMap:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None
        
    def __init__(self):
        self.head = self.Node(None, None)
        self.tail = self.Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = dict()

    def get(self, key):
        if key not in self.map:
            return None
        return self.map[key].val
    
    def put(self, key, val):
        # 若为新插入的节点，则同时插入链表和 map
        if key not in self.map:
            # 插入新的 Node
            node = self.Node(key, val)
            self.add_last_node(node)
            self.map[key] = node
            return
        # 若存在，则替换之前的 val
        self.map[key].val = val

    def remove(self, key):
        # 若 key 本不存在，直接返回
        if key not in self.map:
            return
        # 若 key 存在，则需要同时在哈希表和链表中删除
        node = self.map[key]
        del self.map[key]
        self.remove_node(node)

    def contains_key(self, key):
        return key in self.map
    
    def keys(self):
        key_list = []
        p = self.head.next
        while p != self.tail:
            key_list.append(p.key)
            p = p.next
        return key_list
    
    def add_last_node(self, x):
        temp = self.tail.prev
        # temp <-> tail

        x.next = self.tail
        x.prev = temp
        # temp <- x -> tail

        temp.next = x
        self.tail.prev = x
        # temp <-> x <-> tail

    def remove_node(self, x):
        prev = x.prev
        next = x.next
        # prev <-> x <-> next

        prev.next = next
        next.prev = prev

        x.next = x.prev = None

if __name__ == "__main__":
    map = MyLinkedHashMap()
    map.put("a", 1)
    map.put("b", 2)
    map.put("c", 3)
    map.put("d", 4)
    map.put("e", 5)

    print(map.keys())   # ['a', 'b', 'c', 'd', 'e']
    map.remove("c")
    print(map.keys())   # ['a', 'b', 'd', 'e']