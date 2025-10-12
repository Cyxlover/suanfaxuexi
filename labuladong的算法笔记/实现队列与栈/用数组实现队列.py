# 用数组作为底层数据结构实现栈
class MyArrayStack:
    def __init__(self):
        def __init__(self):
            self.list = []

    # 向栈顶加入元素，时间复杂度O(1)
    def push(self, e):
        self.list.append(e)

    # 从栈顶弹出元素，时间复杂度O(1)
    def pop(self):
        return self.list.pop()

    # 查看栈顶元素，时间复杂度O(1)
    def peek(self):
        return self.list[-1]

    # 返回栈中的元素个数，时间复杂度O(1)
    def size(self):
        return len(self.list)