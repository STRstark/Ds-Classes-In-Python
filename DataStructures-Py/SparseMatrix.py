class SparseMatrix:
    __rows =0
    __cols = 0
    __Index=0
    __Data =[]
    def __init__(self, rows, cols):
        self.__rows = rows  
        self.__cols = cols  
        self.__Data = [None]*rows  
    def GetRow(self):
        return self.__rows
    def GetColumn(self):
        return self.__cols
    def Add(self, i, j, value):
        if i >= self.__rows or j >= self.__cols:
            raise IndexError("Index out of bounds!")
        
        if value != 0:  
            self.__Data[self.__Index]=[i, j, value]

    def Get(self, i, j):
        if i >= self.__rows or j >= self.__cols:
            raise IndexError("Index out of bounds!")
        
        for entry in self.__Data:
            if entry[0] == i and entry[1] == j:
                return entry[2]
        return 0  

    def print_matrix(self):
        x = "Row Index | Column Index | Value"
        print(x ,"\n", "-"*len(x))
        for entry in self.__Data:
            print(f"    {entry[0]}     |      {entry[1]}       |   {entry[2]}")
