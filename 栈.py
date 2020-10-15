# Title: Stack
# Time: 2020/10/15
# Author: Vincent

class Stack():
    def __init__(self):
        self.element = []
    
    def is_empty(self):
        return self.element is None
    
    def push(self, val):
        self.element.append(val)
        return
    
    def pop(self):
        if self.is_empty():
            raise IndexError('空栈，无法弹出元素！')
        return self.element.pop()
    
    def top(self):
        if self.is_empty():
            raise IndexError('空栈，栈顶没有元素！')
        return self.element[-1]
    
    
if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    
    for i in range(10):
        stack.push(i)
    print(stack)
    
    print(stack.pop())
    
    print(stack.top())