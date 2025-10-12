class CycleArray:
    def __init__(self, size = 1):
        self.size = size
        # 因为 Python 支持直接创建泛型数组，所以不需要类型转换
        self.arr = [None] * size
        # start 指向第一个有效元素的索引，闭区间
        self.start = 0
        # 切记 end 是一个开区间
        # 即 end 指向最后一个有效元素的下一个位置索引
        self.end = 0
        self.count = 0

    # 自动扩缩容辅助函数
    def resize(self, newSize):
        # 创建新的数组
        new_arr = [None] * newSize
        # 将旧数组的元素复制到新数组中
        for i in range(self.count):
            new_arr[i] = self.arr[(self.start + i) % self.size]
        self.arr = new_arr
        # 重置 start 和 end 指针
        self.start = 0
        self.end = self.count
        self.size = newSize

    # 在数组头部添加元素，时间复杂度O(1)
    def add_first(self, val):
        # 当数组满时，扩容为原来的两倍
        if self.is_full():
            self.resize(self.size * 2)
        # 因为 start 是闭区间，所以先左移，再赋值
        self.start = (self.start - 1 + self.size) % self.size
        self.arr[self.start] = val
        self.count += 1

    # 删除数组头部元素，时间复杂度O(1)
    def remove_first(self):
        if self.is_empty():
            raise Exception("Array is empty")
        # 因为 start 是闭区间，所以先赋值，再后移
        self.arr[self.start] = None
        self.start = (self.start + 1) % self.size
        self.count -= 1
        # 如果数组元素数量减少到原大小的四分之一，则减小数组大小为一半
        if self.count > 0 and self.count == self.size // 4:
            self.resize(self.size // 2)

    # 在数组尾部添加元素，时间复杂度O(1)
    def add_last(self, val):
        if self.is_full():
            self.resize(self.size * 2)
        # 因为 end 是开区间，所以是先赋值，再后移
        self.arr[self.end] = val
        self.end = (self.end + 1) % self.size
        self.count += 1

    # 删除数组尾部元素，时间复杂度O(1)
    def remove_last(self):
        if self.is_empty():
            raise Exception("Array is empty")
        # 因为 end 是开区间，所以先左移，再赋值
        self.end = (self.end - 1 + self.size) % self.size
        self.arr[self.end] = None
        self.count -= 1
        # 缩容
        if self.count > 0 and self.count == self.size // 4:
            self.resize(self.size // 2)

    # 获取数组头部元素，时间复杂度O(1)
    def get_first(self):
        if self.is_empty():
            raise Exception("Array is empty")
        return self.arr[self.start]

    # 获取数组尾部元素，时间复杂度O(1)
    def get_last(self):
        if self.is_empty():
            raise Exception("Array is empty")
        # end 是开区间，指向的是下一个元素的位置，所以要减1
        return self.arr[(self.end - 1 + self.size) % self.size]

    def is_full(self):
        return self.count == self.size
    
    def size(self):
        return self.count
    
    def is_empty(self):
        return self.count == 0
    