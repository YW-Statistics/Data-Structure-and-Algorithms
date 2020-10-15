# Title: Doubly Linked List
# Author: Vincent
# Time: 2020/10/11

class DoublyListNode():
    def __init__(self, val, prev_=None, next_=None):
        self.val = val
        self.next_ = next_
        self.prev_ = prev_
    
class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.rear = None
    
    # 判空
    def is_empty(self):
        return self.head is None
    
    # 向链表头部插入元素
    def prepend(self, element):
        p = DoublyListNode(element, None, self.head)
        if self.is_empty():
            self.rear = p
        else:
            p.next_.prev_ = p
        self.head = p
        
    # 向链表尾部插入元素
    def append(self, element):
        p = DoublyListNode(element, self.rear, None)
        if self.is_empty():
            self.head = p
        else:
            p.prev_.next_ = p
        self.rear = p
    
    # 获取链表长度
    def get_length(self):
        if self.is_empty():
            return 0
        cur = self.head
        length = 0
        while cur:
            length += 1
            cur = cur.next_
        return length

    # 弹出头部结点
    def pop_first(self):
        if self.is_empty():
            raise ValueError('链表为空，无法进行操作！')
        output = self.head.val
        self.head = self.head.next_
        if self.head: # 链表为空时没有前继结点
            self.head.prev_ = None
        return output
    
    # 弹出尾部结点
    def pop_last(self):
        if self.is_empty():
            raise ValueError('链表为空，无法进行操作！')
        output = self.rear.val
        self.rear = self.rear.prev_
        if self.rear:
            self.rear.next_ = None
        return output
    
    # 在任意位置插入结点
    def insert(self, position, element):
        l = self.get_length()
        if position == 0:
            self.prepend(element)
        elif position == l-1:
            self.append(element)
        elif 0 < position < l-1:
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
        else:
            raise IndexError('下标越界！')

    # 删除指定元素
    def remove(self, element):
        if self.is_empty():
            raise IndexError('下标越界！')
        if self.head.val == element:
            self.head = self.head.next_
            if self.head:
                self.head.prev_ = None
        elif self.rear.val == element:
            self.rear = self.rear.prev_
            if self.rear:
                self.rear.next_ = None
        else:
            cur = self.head
            flag = False
            while cur and cur.val != element:
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
        while cur:
            nums.append(cur.val)
            cur = cur.next_
        return nums
    
    sample = DoublyLinkedList()
    sample.is_empty()
    for i in range(8):
        sample.prepend(i)
    print(testfunction(sample.head))
    
    sample.pop_first()
    print(testfunction(sample.head))
    
    sample.pop_last()
    print(testfunction(sample.head))
    
    sample.insert(3, 8)
    print(testfunction(sample.head))
    
    sample.remove(4)
    print(testfunction(sample.head))
    
    print(sample.get_length())      