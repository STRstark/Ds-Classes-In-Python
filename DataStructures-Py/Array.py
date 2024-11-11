class Array :
    __Data =[] 
    __Flag =[]
    
    Max_Capacity =0
    Size = 0

    def __init__(self,Capacity):
        self.Max_Capacity = Capacity
        self.__Data = [None] * Capacity
        self.__Flag = [False] * Capacity

    def __getitem__(self, index: int) :
        if index > self.Max_Capacity -1 or index <0 :
            raise IndexError("Index Out Of Bounds!!")
        if not self.__Flag[index]:
            raise ValueError(f"No value set at index {index}")
        return self.__Data[index]

    def IsFUll(self):
        return self.Size == self.Max_Capacity
     
    def IsEmpty(self):
        return self.Size == 0
    
    def Add(self, index : int, value):

        if index > self.Max_Capacity -1 or index <0 :
            raise IndexError("Index Out Of Bounds!!")
        if self.IsFUll() :
            raise OverflowError("The Array is FUll!!")
        if not self.__Flag[index] :
            self.__Data[index] = value
            self.__Flag[index] = True
            self.Size = self.Size + 1
            return 
        
        for i in range(index, self.Max_Capacity - 2):
            if not self.__Flag[0]:  
                for j in range(i, index - 1, -1):
                    self.__Data[j + 1] = self.__Data[j]
                    self.__Flag[j + 1] = True
                    self.__Flag[j] = False
                self.__Data[index] = value  
                self.__Flag[index] = True
                self.Size += 1
                return
            
        for i in range(index, 1, -1):
            if not self.__Flag[i - 1]:  
                
                for j in range(i, index):
                    self.__Data[j - 1] = self.__Data[j]
                    self.__Flag[j - 1] = True
                    self.__Flag[j] = False
                self.__Data[index] = value  
                self.__Flag[index] = True
                self.Size += 1
                return
    
    def Delete(self, index: int):
        if index > self.Max_Capacity - 1 or index < 0:
            raise IndexError("Index Out Of Bounds!!")
        if not self.__Flag[index]:
            raise ValueError(f"No value set at index {index} to delete.")
        
        x = self.__Flag[index]
        self.__Data[index] = None
        self.__Flag[index] = False
        self.Size -= 1
        return x
    
    def Print(self):
        for i in range(self.Max_Capacity):
            print("-"*5)
            print(f"| {self.__Data[i]} |  => {i}")
        print("-"*5)
