class Stack :
    
    __Data = []
    __Max_Copacity = 0
    __Top = 0
    
    def __init__(self, Copacity):
        self.__Data = [None] * Copacity
        self.__Max_Capacity = Copacity
        self.__Top = -1
        
    def __str__(self):
        return f"{self.__Data}"
    
    @property
    def Max_Capacity(self):
        return self.__Max_Capacity
    
    def IsFull(self) :
        return self.__Top == self.Max_Capacity-1
    
    def IsEmpty(self) :
        return self.__Top == -1
    
    def Push(self , value):
        if self.IsFull() :
            raise OverflowError("Stack OverFlow")
        
        self.__Top +=1
        self.__Data[self.__Top] = value
    
    def Pop(self):
        if self.IsEmpty() :
            raise OverflowError("Stack UnderFlow")
        
        self.__Top -=1
        return self.__Data[self.__Top +1]
    
    def Peak(self) :
        if self.IsEmpty() :
            raise OverflowError("Stack UnderFlow")
        
        return self.__Data[self.__Top]

    def IncreaseCopacity(self,NewCop):
        self.__Max_Copacity = NewCop
        remaning = NewCop - self.Max_Capacity
        
        while remaning :
            self.__Data.append(None)
            remaning -=1
    
x = Stack(5)
try :
    x.Push("Hello")
    print(x)
    x.IncreaseCopacity(10)
    print(x)
except OverflowError as of : 
    print(of)
    