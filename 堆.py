# Title: Heap
# Time: 2020/10/18
# Author: Vincent

class Heap:
    def __init__(self):
        self.minheap = []
    
    def shift_up(self, new_idx):
        new_val = self.minheap[new_idx]
        while new_idx > 0 and new_val < self.minheap[(new_idx-1)//2]:
            self.minheap[new_idx] = self.minheap[(new_idx-1)//2]
            new_idx = (new_idx-1)//2
        self.minheap[new_idx] = new_val
        
    def shift_down(self, start, end):
        start_val = self.minheap[start]
        while start*2 + 1 <= end:
            child = start*2 + 1
            if child+1 <= end and self.minheap[child] > self.minheap[child+1]:
                child += 1
            if self.minheap[child] < start_val:
                self.minheap[start] = self.minheap[child]
                start = child
            else:
                break
        self.minheap[start] = start_val
    
    def heap_sort(self):
        output = []
        tmp = self.minheap
        while len(self.minheap) > 1:
            self.minheap[0], self.minheap[-1] = self.minheap[-1], self.minheap[0]
            output.append(self.minheap.pop())
            self.shift_down(0, len(self.minheap)-1)
        output.append(self.minheap.pop())
        self.minheap = tmp
        return output
    

if __name__ == '__main__':
    nums = [9,8,7,6,5,4,3,2,1]
    sample = Heap()
    for i in range(len(nums)):
        sample.minheap.append(nums[i])
        sample.shift_up(len(sample.minheap)-1)
    
    print(sample.minheap)
    
    print(sample.heap_sort())
    