# Title: Deuqe
# Time: 2020/10/15
# Author: Vincent

class Deque():
    def __init__(self, init_len=10):
        self.element = [0] * init_len # 初始化队列
        self.len = init_len # 设定存储空间长度
        self.head = 0 # 定义头指针模拟队列左侧弹出操作
        self.nums = 0 # 设定元素数目
    
    def is_empty(self):
        return self.nums == 0
    
    def enqueue(self, val):
        if self.nums == self.len:
            self.extend()
        self.element[(self.head+self.nums) % self.len] = val
        self.nums += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError('队列为空，无法弹出元素！')
        x = self.element[self.head]
        self.head = (self.head+1) % self.len
        self.nums -= 1
        return x
    
    def extend(self):
        old_len = self.len
        self.len *= 2
        new_element = [0]*self.len
        for i in range(old_len):
            new_element[i] = self.element[(self.head+i)%old_len]
        self.element, self.head = new_element, 0
    

if __name__ == '__main__':
    deque = Deque()
    print(deque.is_empty())
    print(deque.nums, deque.len, deque.head)
    
    for i in range(8):
        deque.enqueue(i)
    print(deque.nums, deque.len, deque.head)
    
    print(deque.dequeue())
    print(deque.nums, deque.len, deque.head)
    
    for i in range(10):
        deque.enqueue(i)
    print(deque.nums, deque.len, deque.head)