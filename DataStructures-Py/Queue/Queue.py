class Queue:
    __Data = []
    __Max_Capacity = 0
    __Front = 0
    __Rear = 0
    
    @property
    def Front(self):
        return self.__Front
    @property
    def Rear(self):
        return self.__Rear
    @property
    def Cap(self):
        return self.__Max_Capacity
    
    def __init__(self ,Max_Capacity ):
        self.__Max_Capacity = Max_Capacity
        self.__Data = [None] * Max_Capacity
        
    def __str__(self):
        return f"{self.__Data}"
    
    def IsEmpty(self):
        return self.__Front == self.__Rear
    
    def IsFull(self):
        return self.__Rear == self.__Max_Capacity
    
    def EnQueue(self , Value):
        if self.IsFull():
            raise OverflowError("Queue is full")
        
        self.__Data[self.__Rear] = Value
        self.__Rear +=1
        
    def DeQueue(self):
        if self.IsEmpty():
            raise IndexError("Dequeue from an empty queue")
        
        self.__Front+=1
        return self.__Data[self.__Front -1]
    
    def Peak(self):
        if self.IsEmpty():
            raise IndexError("Dequeue from an empty queue")
        
        return self.__Data[self.__Front]


def MergeSortedQueue(A :Queue , B : Queue):
    
    CacheA = A
    CacheB = B
    MergedQueue = Queue(A.Cap + B.Cap)
    while (not CacheA.IsEmpty()) and (not CacheB.IsEmpty()):
        if CacheA.Peak() < CacheB.Peak():
            MergedQueue.EnQueue(CacheA.DeQueue())    
        else:
            MergedQueue.EnQueue(CacheB.DeQueue())
    while (not CacheA.IsEmpty()):
        MergedQueue.EnQueue(CacheA.DeQueue())    
    while (not CacheB.IsEmpty()):
        MergedQueue.EnQueue(CacheB.DeQueue())    
    return MergedQueue

X = Queue(5)
Y = Queue(6)
X.EnQueue(0)
X.EnQueue(1)
X.EnQueue(4)
Y.EnQueue(0)
Y.EnQueue(1)
Y.EnQueue(3)
print(X.Peak())
print (X , Y)
print(MergeSortedQueue(X,Y))