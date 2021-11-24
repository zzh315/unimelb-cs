# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

class PriorityQueue():
    def __init__(self, h=[]):
        self.heap = []
        self.dic = {}
        if h:
            self.heap = h[:]
            for index, (p, i) in enumerate(h):
                self.dic[i] = index
            self.heapify()
    
    def __len__(self):
        return len(self.heap)
        
    def __str__(self):
        return str(self.heap)
    
    def __contains__(self, item):
        return item in self.dic
    
    def empty(self):
        return len(self) == 0
    
    def put(self, item, priority=0):
        self.dic[item] = len(self)
        self.heap.append((priority, item))
        self._siftdown(len(self) - 1)
    
    def get(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.dic[self.heap[0][1]] = 0
        priority, item = self.heap.pop()
        self.dic.pop(item)
        self._siftup(0)
        return item, priority
    
    def update(self, item, priority):
        index = self.dic[item]
        self.heap[index] = (priority, item)
        self._siftup(index)
        self._siftdown(index)
    
    def heapify(self):
        for i in reversed(range(0, len(self) // 2)):
            self._siftup(i)
    
    def _siftdown(self, index):
        if index > 0 and self.heap[index] < self.heap[(index - 1) // 2]:
            self.heap[index], self.heap[(index - 1) // 2] = self.heap[(index - 1) // 2], self.heap[index]
            self.dic[self.heap[index][1]] = index
            self.dic[self.heap[(index - 1) // 2][1]] = (index - 1) // 2
            self._siftdown((index - 1) // 2)
    
    def _siftup(self, index):
        swap = False
        if index * 2 + 1 < len(self) and self.heap[index] > self.heap[index * 2 + 1]:
            swap = True
            target = 2 * index + 1
        if index * 2 + 2 < len(self) and min(self.heap[index], self.heap[index * 2 + 1]) > self.heap[index * 2 + 2]:
            swap = True
            target = 2 * index + 2
        if swap:
            self.heap[index], self.heap[target] = self.heap[target], self.heap[index]
            self.dic[self.heap[index][1]] = index
            self.dic[self.heap[target][1]] = target
            self._siftup(target)


def test():
    h = PriorityQueue()
    h.put(1, 30)
    h.put(2, 50)
    h.put(3, 20)
    h.put(4, 60)
    h.put(5, 45)
    h.put(6, 55)
    h.put(7, 25)
    h.put(8, 35)
    print(h)
    print(h.get())
    print(h)
    h.update(5, 15)
    print(h)
    
if __name__ == "__main__":
    test()
