# Title: One-way Circular Linked List
# Author: Vincent
# Time: 2020/10/10

class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class OneWayCircularLinkedList():
    def __init__(self):
        self.rear = None
    
    # 判断链表是否为空
    def is_empty(self):
        return self.rear is None
    
    # 在链表头部插入元素
    def prepend(self, val):
        # 若头部结点为空，那么头尾结点相同
        p = ListNode(val)
        if self.is_empty():
            p.next = p
            self.rear = p
        else:
            p.next = self.rear.next
            self.rear.next = p
            
    # 在链表尾部插入元素
    def append(self, val):
        p = ListNode(val)
        if self.is_empty():
            p = p.next
            self.rear = p
        else:
            p.next = self.rear.next
            self.rear.next = p
            self.rear = self.rear.next
    
    # 计算链表长度
    def get_length(self):
        if self.is_empty():
            return 0
        cur = self.rear
        length = 1
        while cur.next != self.rear:
            length += 1
            cur = cur.next
        return length
    
    # 弹出尾部元素
    def pop_last(self):
        if self.is_empty():
            raise ValueError('self.rear 必须非空')
        # 链表只有一个元素时预先判断
        if self.rear.next == self.rear: 
            output = self.rear.val
            self.rear = None
            return output
        cur = self.rear
        while cur.next != self.rear:
            cur = cur.next
        output = cur.next.val
        cur.next = cur.next.next # 删除尾部节点
        self.rear = cur
        return output
    
    # 在指定位置添加元素
    def insert(self, position, element):
        p = ListNode(element)
        l = self.get_length()
        if position >= l or position < 0:
            raise ValueError('超出了链表长度范围！')
        
        # 判空
        if self.is_empty():
            if position > 0:
                raise ValueError('链表为空，且没有在位置0添加元素！')
            else:
                p.next = p
                self.rear = p
                return
        
        # 分三种情况添加元素
        if position == 0:
            self.prepend(element)
        elif position == l - 1:
            self.append(element)
        else:
            cur = self.rear
            while position > 0:
                cur = cur.next
                position -= 1
            p.next = cur.next
            cur.next = p
        
    # 删除指定元素
    def remove(self, element):
        if self.is_empty():
            raise ValueError('self.rear 必须非空')
        cur = self.rear
        flag = False # 标记是否链表含有指定元素
        if self.rear.val == element:
            flag = True
            if self.rear.next == self.rear: 
                output = self.rear.val
                self.rear = None
                return output
            else:
                cur = self.rear
                while cur.next != self.rear:
                    cur = cur.next
                cur.next = cur.next.next # 删除尾部节点
                self.rear = cur
        else:
            while cur.next.val != element and cur.next != self.rear:
                cur = cur.next
                if cur.next.val == element:
                    flag = True
                    
            if not flag:
                raise ValueError('链表中不存在该元素！')
            cur.next = cur.next.next
                
    
        
if __name__ == '__main__':
    def testfunction(node):
        nums = []
        cur = node.next
        while cur != node:
            nums.append(cur.val)
            cur = cur.next
        nums.append(cur.val)
        return nums
    
    sample = OneWayCircularLinkedList()
    for i in range(8):
        sample.prepend(i)
    print(testfunction(sample.rear))
    
    sample.append(2)
    print(testfunction(sample.rear))
    
    print(sample.get_length())
    
    print(sample.pop_last())
    
    sample.insert(1, 10)
    print(testfunction(sample.rear))
    
    sample.remove(0)
    print(testfunction(sample.rear))