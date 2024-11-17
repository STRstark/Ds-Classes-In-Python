class Queue:
    __Data = []
    __Max_Capacity = 0
    __Front = 0
    __Rear = 0
    __Size = 0
    
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
        return self.__Size == 0
    
    def IsFull(self):
        return self.__Size == self.__Max_Capacity
    
    def EnQueue(self , Value):
        if self.IsFull():
            raise OverflowError("Queue is full")
        
        self.__Data[self.__Rear] = Value
        self.__Rear = (self.__Rear +1) % self.__Max_Capacity
        self.__Size +=1
        
    def DeQueue(self):
        if self.IsEmpty():
            raise IndexError("Dequeue from an empty queue")
        
        self.__Size-=1
        self.__Front =( self.__Front + 1) % self.__Max_Capacity
        return self.__Data[self.__Front -1]
    
    
    def Peak(self):
        if self.IsEmpty():
            raise IndexError("Dequeue from an empty queue")
        
        return self.__Data[self.__Front]


def DeleteMaxElement(X : Queue):
    #Findig the Value of the maximum element inside the queue:
    Data = []
    while not X.IsEmpty():
        Data.append(X.DeQueue())
    MAX = max(Data)
    Data.remove(MAX)
    
    for i in Data :
        X.EnQueue(i)  
    return X  
        
X = Queue(5)
X.EnQueue(1)
X.EnQueue(2)
X.EnQueue(3)
X.EnQueue(4)
X.EnQueue(5)
print(X)
print(DeleteMaxElement(X))