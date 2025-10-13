from labuladong的算法笔记.实现动态数组.实现环形数组 import CycleArray
# TODO: 一样是实现不了，只是为了不报错，后面再解决

class MyArrayDeque:
    def __init__(self):
        self.arr = CycleArray()

    # 从队头插入元素，时间复杂度 O(1)
    def add_first(self, e):
        self.arr.add_first(e)

    # 从队尾插入元素，时间复杂度 O(1)
    def add_last(self, e):
        self.arr.add_last(e)

    # 从队头删除元素，时间复杂度 O(1)
    def remove_first(self):
        return self.arr.remove_first()

    # 从队尾删除元素，时间复杂度 O(1)
    def remove_last(self):
        return self.arr.remove_last()

    # 查看队头元素，时间复杂度 O(1)
    def peek_first(self):
        return self.arr.get_first()

    # 查看队尾元素，时间复杂度 O(1)
    def peek_last(self):
        return self.arr.get_last()