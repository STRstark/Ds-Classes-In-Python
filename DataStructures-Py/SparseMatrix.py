class SparseMatrix:
    __Size = 0
    __Rows = 0
    __Cols = 0
    __Index = 0
    __Data = []

    def __init__(self, rows , cols , Size) :
        self.__Rows = rows
        self.__Cols = cols
        self.__Data = [None] * Size
        self.__Size = Size
    
    def __str__(self):
        x = "Row Index | Column Index | Value"
        x += '\n'
        x+="---------------------------------"
        x += '\n'
        for entry in self.__Data:
            if(entry is None):
                break
            x+=f"    {entry[0]}     |      {entry[1]}       |   {entry[2]} \n"     
            x+="---------------------------------\n"
       
        return x
    def __getitem__(self , Index):
        return self.__Data[Index]
    
    @property
    def Size(self):
        return self.__Size
    @property
    def Index(self):
        return self.__Index
    
    def GetRow(self):
        return self.__Rows
    
    def GetColumn(self):
        return self.__Cols
    
    def Add(self, i , j, value) :
        if self.__Index == self.__Rows :
            raise OverflowError("Out of memory")
        
        if i <0 or j <0 or i > self.__Rows or j >  self.__Cols :
            raise IndexError("Index out of bounds!")
        if(value == 0):
            raise ValueError("Value can not be zero")
        
        for index in range(0 ,self.__Index):
            if self.__Data[index][0] == i and self.__Data[index][1] == j:
                if self.__Data[index][2] != value :
                    raise ValueError("This value Exist in the matrix , try changing it")
                else :
                    return
                
        self.__Data[self.__Index] = [i, j , value]
        self.__Index +=1
            
    def Remove(self , i , j):
        if i <0 or j <0 or i >self.__Rows or j > self.__Cols :
            raise IndexError("Index out of bounds!")
        X=0
        for index in range(self.__Size):
            if self.__Data[index][0] == i and self.__Data[index][1] == j :
                X = self.__Data[2]
                for IndexAfter in range(index , self.__Size-1):
                    self.__Data[IndexAfter] = self.__Data[IndexAfter+1]
                self.__Index-=1
                return X
        raise ValueError(f"No item is saved at {i} - {j}")
            
    def Get(self , i , j):
        if i <0 or j <0 or i >self.__Rows or j >self.__Cols :
            raise IndexError("Index out of bounds!")
        for entry in self.__Data:
            if entry == None :
                break
            if entry[0] == i and entry[1] == j :
                return entry
        
        raise ValueError(f"No item is saved at {i} - {j}")
    
    def Find(self , i , j):
        if i <0 or j <0 or i >self.__Rows or j >self.__Cols :
            return False
        for entry in self.__Data:
            if entry == None :
                return False
            if entry[0] == i and entry[1] == j :
                return True
    
def SumSparsMatrises(A : SparseMatrix , B : SparseMatrix):
    CacheA = A
    CacheB = B
    S = SparseMatrix(CacheA.GetRow() + CacheB.GetRow() , CacheA.GetColumn() + CacheB.GetColumn() ,CacheA.Size + CacheB.Size )
    Added = False
    for i in range(CacheA.Index):
        if Added :
            Added = False
            i-=1
        if CacheB.Find(CacheA[i][0] , CacheA[i][1]):
            S.Add(CacheA[i][0] , CacheA[i][1] , CacheA[i][2] + CacheB[i][2])
            CacheA.Remove(CacheA[i][0] , CacheA[i][1])
            CacheB.Remove(CacheB[i][0] , CacheB[i][1])
            Added = True
    for i in range(CacheA.Index):
        S.Add(CacheA[i][0],CacheA[i][1],CacheA[i][2])
    for i in range(CacheB.Index):
        S.Add(CacheB[i][0],CacheB[i][1],CacheB[i][2])
    return S



X = SparseMatrix(2, 3, 6)
Y = SparseMatrix(2, 3, 6)
X.Add(1, 1, 7)
X.Add(1, 2, 8)
Y.Add(1, 1, 8)
Y.Add(1, 2, 9)
print(X)
print(Y)
print(SumSparsMatrises(X,Y))