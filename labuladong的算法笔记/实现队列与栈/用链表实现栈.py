from collections import deque

# 用链表作为底层数据结构实现栈
# Python 的 deque 就是双链表
class MyLinkedStack:
    def __init__(self):
        self.list = deque()

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

    
if __name__ == "__main__":
    stack = MyLinkedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())      # 3
    print(stack.peek())     # 2
    print(stack.size())     # 2
