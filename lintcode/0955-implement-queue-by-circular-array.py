# Description
# 中文
# English
# Implement queue by circulant array. You need to support the following methods:

# CircularQueue(n): initialize a circular array with size n to store elements
# boolean isFull(): return true if the array is full
# boolean isEmpty(): return true if there is no element in the array
# void enqueue(element): add an element to the queue
# int dequeue(): pop an element from the queue
# it's guaranteed in the test cases we won't call enqueue if it's full and we also won't call dequeue if it's empty. So it's ok to raise exception in scenarios described above.

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input:
# CircularQueue(5)
# isFull()
# isEmpty()
# enqueue(1)
# enqueue(2)
# dequeue()
# Output:
# ["false","true","1"]
# Example 2:

# Input:
# CircularQueue(5)
# isFull()
# isEmpty()
# enqueue(1)
# enqueue(2)
# dequeue()
# dequeue()
# enqueue(1)
# enqueue(2)
# enqueue(3)
# enqueue(4)
# enqueue(5)
# isFull()
# dequeue()
# dequeue()
# dequeue()
# dequeue()
# dequeue()
# Output:
# ["false","true","1","2","true","1","2","3","4","5"]

class CircularQueue:
    def __init__(self, n):
        self.circularArray = [0]*n
        self.front = 0
        self.rear = 0
        self.size = 0
        
    """
    @return:  return true if the array is full
    """
    def isFull(self):
        return self.size == len(self.circularArray)

    """
    @return: return true if there is no element in the array
    """
    def isEmpty(self):
        return self.size == 0

    """
    @param element: the element given to be added
    @return: nothing
    """
    def enqueue(self, element):
        if self.isFull():
            raise RuntimeError("Queue is already full")
        self.rear = (self.front+self.size) % len(self.circularArray)
        self.circularArray[self.rear] = element
        self.size += 1

    """
    @return: pop an element from the queue
    """
    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Queue is already empty")
        ele = self.circularArray[self.front]
        self.front = (self.front+1) % len(self.circularArray)
        self.size -= 1
        return ele