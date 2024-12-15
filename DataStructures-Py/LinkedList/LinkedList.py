class Node :
    def __init__(self , Value , nex_node = None):
        self.Value = Value
        self.next_node = nex_node
        
class LinkedList :
    
    def __init__(self , datatype = int):
        self.Head = None
        self.datatype = datatype
    def __str__(self):
        
        temp_node = self.Head
        result = ""
        while temp_node:
            result += str(temp_node.Value)
            if temp_node.next_node is not None:
                result += " -> "
            temp_node = temp_node.next_node
        return result
    
    def Insert(self , value):
        if not isinstance(value , self.datatype):
            raise TypeError(f"linkedList only accepts data of type :{self.datatype}!")
        
        if self.Head is None :
            self.Head = Node(value)
            return 
        
        Current = self.Head
        
        while Current.next_node is not None:
            Current = Current.next_node
            
        Current.next_node = Node(value)
    
    
    def DeletNext(self , Node : Node):
        Current = self.Head
        
        while Current.next_node is not None :
            if Current == Node:
                Current.next_node = Current.next_node.next_node
                return
            Current = Current.next_node
        
    def DeleteANode(self, Node:Node):
        if Node is None : 
            raise ValueError('Can not delete a null node !')
        if self.Head == Node:
            self.Head = self.Head.next_node
            return
        
        Current = self.Head
        while Current.next_node is not None :
            if Current.next_node == None :
                Current = Current.next_node.next_node
            Current = Current.next_Node
    
    def DeleteAnIndex(self , Index : int):
        Current = self.Head
        
        for _ in range(Index):
            Current = Current.next_Node
        
        self.DeleteANode(Current)

    def DeleteAValue(self , value) :
        self.DeleteANode(self.GetNodeWithValue(value))

def MergeSorted(List1 :LinkedList , List2 : LinkedList):
    merged_list = LinkedList(List1.datatype)
    
    current1 = List1.Head
    current2 = List2.Head
    
    while current1 and current2:
        if current1.Value < current2.Value:
            merged_list.Insert(current1.Value)
            current1 = current1.next_node
        else:
            merged_list.Insert(current2.Value)
            current2 = current2.next_node
    
    while current1:
        merged_list.Insert(current1.Value)
        current1 = current1.next_node
    
    while current2:
        merged_list.Insert(current2.Value)
        current2 = current2.next_node
    
    return merged_list


test = LinkedList(int)

test.Insert(5)
test.Insert(6)
test.Insert(7)
test.Insert(8)
test.Insert(9)
test.Insert(10)
test.Insert(8)

print(test) 
test.DeleteANode(test.GetNodeWithValue(5))

print(test)
