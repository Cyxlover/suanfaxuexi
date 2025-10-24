class MyArrayList:
    # 默认初始容量
    INIT_CAP = 1

    def __init__(self, init_capacity=None):
        self.data = [None] * (init_capacity if init_capacity is not None else self.__class__.INIT_CAP)  # 如果init_capacity不是空的就初始化，如果是空的，使用默认初始化函数 self.__class__.INIT_CAP
        self.size = 0

    # 增manl
    def add_last(self, e):      # 在数组最后加元素
        cap = len(self.data)    # 获取data的长度，将其储存进cap里
        # 看 data 数组容量够不够
        if self.size == cap:    # 如果数组满了
            self._resize(2 * cap)   # 将数组的容量扩大两倍
        # 在尾部插入元素
        self.data[self.size] = e    # 尾部插入 e（element）
        self.size += 1      # 数组的元素个数加一
    
    def add(self, index, e):    # 在数组的任何位置加元素
        # 检查索引越界
        self._check_position_index(index)   # 使用_check_position_index函数检查索引是否越界，返回一个布尔值

        cap = len(self.data)    # 获取data的长度，将其储存进cap里
        # 看 data 数组容量够不够
        if self.size == cap:    # 如果数组满了
            self._resize(2 * cap)   # 将数组的容量扩大两倍

        # 搬移数据 data[index..] -> data[index+1..]
        # 给新元素腾出位置
        for i in range(self.size-1, index-1, -1):   # 使用循环将数组往后退一格
            self.data[i+1] = self.data[i]   # 后面元素等于前一元素

        # 插入新元素
        self.data[index] = e    # 将e插入数组
        
        self.size += 1  # 数组元素个数加一

    def add_first(self, e):     # 在数组开头插入元素
        self.add(0, e)      # 将e插入数组开头

    # 删
    def remove_last(self):      # 把最后一个元素删除
        if self.size == 0:      # 如果数组为空
            raise Exception("NoSuchElementException")   # 报错
        cap = len(self.data)    # 将data的长度赋给cap
        # 可以缩容， 节约空间
        if self.size == cap // 4:   # 如果cap等于1/4数组长度
            self._resize(cap // 2)  # 将数组长度缩小两倍

        deleted_val = self.data[self.size - 1]  # 将数组最后一个元素赋给deleted_val（后面可以打印出来看看删了什么）
        # 删除最后一个元素
        self.data[self.size - 1] = None     # 将最后一个元素变为None（不会被指，防止内存泄漏）
        self.size -= 1      # 数组长度减一

        return deleted_val      # 看看删了什么东西
    
    def remove(self, index):    # 哪里的元素都能删O(n)
        # 检查索引越界
        self._check_element_index(index)    # 看看索引是否合法

        cap = len(self.data)    # 将数组的长度赋给cap
        # 可以缩容， 节约空间
        if self.size == cap // 4:   
            self._resize(cap // 2)

        deleted_val = self.data[index]  # 把要删除的元素赋给deleted_val

        # 搬移数据 data[index+1..] -> data[index..]
        for i in range(index + 1, self.size):   # 把删除元素后面的元素前移
            self.data[i - 1] = self.data[i]     # 前等于后

        self.data[self.size - 1] = None     # 将删除元素赋值为None
        self.size -= 1  # 元素个数减一

        return deleted_val
    
    def remove_first(self):     # 直接将数组的第一个元素返回
        return self.remove(0)

    # 查
    def get(self, index):       # 把查到的元素返回
        # 检查索引越界
        self._check_element_index(index)    # 看看索引是否合法

        return self.data[index]

    # 改
    def set(self, index, element):      # 将index位置的元素替换为element
        # 检查索引越界
        self._check_element_index(index)    # 看看索引对应的元素是否合法
        # 修改数据
        old_val = self.data[index]      # 把被改的那个元素赋给old_val，后面可以看看把什么换了
        self.data[index] = element
        return old_val
    
    # 工具方法
    def get_size(self):     # 返回数组长度
        return self.size
    
    def is_empty(self):     # 如果数组是空的，返回长度为0
        return self.size == 0
    
    # 将 data 的容量改为 newCap
    def _resize(self, new_cap):     # 数组搬家
        temp = [None] * new_cap     # 建立新数组
        for i in range(self.size):  # 遍历数组
            temp[i] = self.data[i]  # 用temp临时将数组储存起来
        self.data = temp

    def _is_element_index(self, index): # 判断索引对应的元素是否越界，返回布尔值
        return 0 <= index < self.size
    
    def _is_position_index(self, index):    # 判断索引对应的位置是否越界，返回布尔值
        return 0 <= index <= self.size
    
    def _check_element_index(self, index):  # 判断索引对应的元素是否越界，返回报错
        if not self._is_element_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def _check_position_index(self, index): # 判断索引对应的位置是否越界，返回报错
        if not self._is_position_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def display(self):
        print(f"size = {self.size}, cap = {len(self.data)}")    # 打印当前数组实际储存元素，打印底层数组容量
        print(self.data)


# Usage example
if __name__ == "__main__":
    arr = MyArrayList(init_capacity=3)

    # 添加 5 个元素
    for i in range(1, 6):
        arr.add_last(i)

    arr.remove(3)
    arr.add(1, 9)
    arr.add_first(100)
    val = arr.remove_last()

    # 100 1 9 2 3
    for i in range(arr.get_size()):
        print(arr.get(i))