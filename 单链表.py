# Title: Single Linked List
# Author: Vincent
# Time: 2020/10/10

class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class SingleLinkedList():
    def __init__(self):
        self.head = None
    
    # 判断链表是否为空
    def isempty(self):
        return self.head is None
    
    # 头插法
    def prepend(self, val):
        self.head = ListNode(val, self.head)
    
    # 删除链表
    def delete(self):
        self.head = None
    
    # 向链表某个位置插入结点
    def insert(self, destination, element):
        if not self.head:
            raise ValueError('self.head 必须非空')
        sentinel = ListNode(0) # 设置哨兵
        sentinel.next = self.head
        cur = sentinel
        while destination >= 0:
            cur = cur.next
            destination -= 1
        tmp = cur.next
        cur.next = ListNode(element)
        cur.next.next = tmp
        return sentinel.next
    
    # 计算链表长度
    def get_length(self):
        if not self.head:
            return 0
        cur = self.head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        return length
    
    # 删除头节点
    def del_firstnode(self):
        if not self.head:
            raise ValueError('self.head 必须非空')
        self.head = self.head.next
    
    # 删除某个位置的结点
    def del_anynode(self, position):
        if not self.head:
            raise ValueError('self.head 必须非空')
        sentinel = ListNode(0)
        sentinel.next = self.head
        cur = sentinel
        while position > 0:
            position -= 1
            cur = cur.next
        cur.next = cur.next.next
        return sentinel.next

if __name__ == '__main__':
    def testfunction(node):
        nums = []
        cur = node
        while cur:
            nums.append(cur.val)
            cur = cur.next
        return nums
    
    sample = SingleLinkedList()
    sample.isempty()
    for i in range(8):
        sample.prepend(i)
    print(testfunction(sample.head))
    sample.insert(2, 3)
    print(testfunction(sample.head))
    print(sample.get_length())
    sample.del_firstnode()
    print(testfunction(sample.head))
    sample.del_anynode(1)
    print(testfunction(sample.head))
    sample.delete()
    print(testfunction(sample.head))    