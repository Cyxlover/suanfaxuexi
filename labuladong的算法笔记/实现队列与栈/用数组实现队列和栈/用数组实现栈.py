from labuladong的算法笔记.实现动态数组.实现环形数组 import CycleArray 
# TODO: 实际上运行不了，只是为了不报错，待以后解决

class MyArrayQueue:
    def __init__(self):
        self.arr = CycleArray()

    def push(self, t):
        self.arr.add_last(t)

    def pop(self):
        return self.arr.remove_first()

    def peek(self):
        return self.arr.get_first()

    def size(self):
        return self.arr.size()