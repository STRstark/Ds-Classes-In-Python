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
        return self.__Data[self.__Rear -1]
    
    def Peak(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        
        return self.__Data[self.__Rear]

X = Queue(5)
try :
    
    print(X)
    X.EnQueue(50)
    print(X)
    X.EnQueue(100)
    print(X)
    X.DeQueue()
    print(X)
    X.EnQueue(100)
    print(X)
    X.DeQueue()
    print(X)
    print(X.Front)

except OverflowError as of : 
    print(of)
    