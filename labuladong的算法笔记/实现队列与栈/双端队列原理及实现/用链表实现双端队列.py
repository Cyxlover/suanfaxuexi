from labuladong的算法笔记.实现单双链表.实现双链表 import MyLinkedList
# TODO: 一样还是实现不了，只是为了不报错

class MyListDeque:
    def __init__(self):
        # 使用我们之前实现的 'MyLinkedList' 类
        self.list = MyLinkedList()

    # 从队头插入元素，时间复杂度 O(1)
    def add_first(self, e):
        self.list.add_first(e)

    # 从队尾插入元素，时间复杂度 O(1)
    def add_last(self, e):
        self.list.add_last(e)

    # 从队头删除元素，时间复杂度 O(1)
    def remove_first(self):
        return self.list.remove_first()

    # 从队尾删除元素，时间复杂度 O(1)
    def remove_last(self):
        return self.list.remove_last()

    # 查看队头元素，时间复杂度 O(1)
    def peek_first(self):
        return self.list.get_first()

    # 查看队尾元素，时间复杂度 O(1)
    def peek_last(self):
        return self.list.get_last()
    
# 使用示例
my_deque = MyListDeque()

my_deque.add_first(1)
my_deque.add_first(2)
my_deque.add_last(3)
my_deque.add_last(4)

print(my_deque.remove_first())  # 2
print(my_deque.remove_last())   # 4
print(my_deque.peek_first())    # 1
print(my_deque.peek_last())     # 3