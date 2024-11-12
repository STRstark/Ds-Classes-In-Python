class Stack:
    __Data =[]
    __Max_Capacity = 0
    __Top = -1
    
    def __init__(self , capacity):
        self.__Data = [None] * capacity
        self.__Max_Capacity = capacity
        
    def __str__(self):
        return f"{self.__Data}"
    
    def IsFull(self) :
        return self.__Top == self.__Max_Capacity-1
    
    def IsEmpty(self) :
        return self.__Top == -1
    
    def Push(self , value) :
        if self.IsFull() :
            raise OverflowError("Stack OverFlow")    
        
        self.__Top +=1
        self.__Data[self.__Top] = value
        
    def Pop(self):
        if self.IsEmpty() :
            raise OverflowError("Stack UnderFlow , You are trying to pop from an empty list")
        
        self.__Top -=1
        return self.__Data[self.__Top+1]
    
    def Peak(self):
        if self.IsEmpty() :
            raise OverflowError("Stack UnderFlow , You are trying to peak from an empty list")
        
        return self.__Data[self.__Top]

    def IncreaseCopacity(self,NewCop):
        remaning = NewCop - self.__Max_Capacity
        
        while remaning :
            self.__Data.append(None)
            remaning -=1
        
        self.__Max_Capacity = NewCop
            
    def DecreaseCopacity(self , NewCap):
        if NewCap < self.__Top:
            raise ValueError("Can not deacrese the capacity less than the count of values inside the stack")
        remaning = self.__Max_Capacity - NewCap
        while remaning :
            self.__Data.pop()
            remaning -=1
        self.__Max_Capacity = NewCap

x = Stack(5)
try :
    x.Push("Hello")
    print(x)
    x.IncreaseCopacity(10)
    print(x)
except OverflowError as of : 
    print(of)
    