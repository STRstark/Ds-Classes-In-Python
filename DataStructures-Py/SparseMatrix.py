class SparseMatrix:
    __Rows = 0
    __Cols = 0
    __Index = 0
    __Data = []

    def __init__(self, rows , cols) :
        self.__Rows = rows
        self.__Cols = cols
        self.__Data = [None] * rows

    def GetRow(self):
        return self.__Rows
    
    def GetColumn(self):
        return self.__cols
    

    def Add(self, i , j, value) :
        if self.__Index == self.__Rows :
            raise OverflowError("Out of memory")
        
        if i <0 or j <0 or i >=self.__Rows or j >= self.__Cols :
            raise IndexError("Index out of bounds!")
        if(value == 0):
            raise ValueError("Value can not be zero")
        
        for i in range(0 ,self.__Index):
            if self.__Data[i][0] == i and self.__Data[i][1] == j:
                if self.__Data[i][2] != value :
                    raise ValueError("This value Exist in the matrix , try changing it")
                else :
                    return
                
        self.__Data[self.__Index] = [i, j , value]
        self.__Index +=1

    def Get(self , i , j):
        if i <0 or j <0 or i >=self.__Rows or j >= self.__Cols :
            raise IndexError("Index out of bounds!")
        for entry in self.__Data:
            if entry == None :
                break
            if entry[0] == i and entry[1] == j :
                return entry
        
        raise ValueError(f"No item is saved at {i} - {j}")
        
    def print_matrix(self):
        x = "Row Index | Column Index | Value"
        print(x ,"\n", "-"*len(x))
        for entry in self.__Data:
            print(f"    {entry[0]}     |      {entry[1]}       |   {entry[2]}")
