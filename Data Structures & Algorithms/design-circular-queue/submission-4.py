class MyCircularQueue:

    def __init__(self, k: int):
        self.cqueue = [-1]*k
        self.front = self.rear = -1
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isEmpty():
            self.rear = self.front = 0
            self.cqueue[self.rear] = value
            return True
        if self.isFull():
            return False
        self.rear = (self.rear + 1)%self.k
        self.cqueue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.front == -1:
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.cqueue[self.front] = -1
            self.front = (self.front + 1)%self.k
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.cqueue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.cqueue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear == self.k-1 and self.front == 0) or (self.front == self.rear+1)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()