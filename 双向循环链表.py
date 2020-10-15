# Title: Double Circular Linked List
# Author: Vincent
# Time: 2020/10/12

class DoublyListNode():
    def __init__(self, val, prev_=None, next_=None):
        self.val = val
        self.next_ = next_
        self.prev_ = prev_
        
class DoubleCircularLinkedList():
    
    def __init__(self):
        self.rear = None
        self.head = None
        
    # 判断链表是否为空
    def is_empty(self):
        return self.rear is None
    
    # 向头部插入元素
    def prepend(self, element):
        p = DoublyListNode(element, None, self.head)
        if self.is_empty():
            self.rear = p
        else:
            p.next_.prev_ = p
        self.head = p
        self.rear.next_ = self.head
        self.head.prev_ = self.rear
    
    # 向尾部插入元素
    def append(self, element):
        p = DoublyListNode(element, self.rear, None)
        if self.is_empty():
            self.head = p
        else:
            p.prev_.next_ = p
        self.rear = p
        self.rear.next_ = self.head
        self.head.prev_ = self.rear
        
    # 弹出头部元素
    def pop_first(self):
        if self.is_empty():
            raise ValueError('链表为空，该操作无效！')
        output = self.head.val
        self.head = self.head.next_
        if self.head:
            self.head.prev_ = self.rear
            self.rear.next_ = self.head
        return output
    
    # 弹出尾部元素
    def pop_last(self):
        if self.is_empty():
            raise ValueError('链表为空，该操作无效！')
        output = self.rear.val
        self.rear = self.rear.prev_
        if self.rear:
            self.rear.next_ = self.head
            self.head.prev_ = self.rear
        return output
    
    # 获取链表长度
    def get_length(self):
        if self.is_empty():
            return 0
        cur = self.head
        length = 1
        while cur.next_ != self.head:
            cur = cur.next_
            length += 1
        return length
    
    # 向指定位置插入任意元素
    def insert(self, position, element):
        l = self.get_length()
        if position >= l or position < 0:
            raise IndexError('下标越界！')
        elif position == 0:
            self.prepend(element)
        elif position == l-1:
            self.append(element)
        else:
            if self.is_empty():
                raise IndexError('下标越界！')
            if position <= l / 2:
                cur = self.head
                while position > 0:
                    cur = cur.next_
                    position -= 1
                p = DoublyListNode(element, None, cur)
                cur.prev_.next_ = p
            else:
                cur = self.rear
                while position < l-1:
                    cur = cur.prev_
                    position += 1
                p = DoublyListNode(element, None, cur)
                cur.prev_.next_ = p
    
    # 删除指定元素
    def remove(self, element):
        if self.is_empty():
            raise IndexError('下标越界！')
        if self.head.val == element:
            self.head = self.head.next_
            if self.head:
                self.head.prev_ = self.rear
        elif self.rear.val == element:
            self.rear = self.rear.prev_
            if self.rear:
                self.rear.next_ = self.head
        else:
            cur = self.head
            flag = False
            while cur.val != element and cur.next_ != self.head:
                cur = cur.next_
                if cur and cur.val == element:
                    flag = True
            if flag:
                cur.prev_.next_ = cur.next_
            else:
                raise ValueError('链表中不存在该元素！')
    

if __name__ == '__main__':
    def testfunction(node):
        nums = []
        cur = node
        while cur.next_ != node:
            nums.append(cur.val)
            cur = cur.next_
        nums.append(cur.val)
        return nums
    
    sample = DoubleCircularLinkedList()
    for i in range(8):
        sample.prepend(i)
    print(testfunction(sample.head))
    
    sample.append(2)
    print(testfunction(sample.head))
    
    print(sample.get_length())
    
    print(sample.pop_last())
    print(testfunction(sample.head))
    
    sample.insert(1, 10)
    print(testfunction(sample.head))
    
    sample.remove(1)
    print(testfunction(sample.head))    