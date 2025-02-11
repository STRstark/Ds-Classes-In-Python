class Node :
    def __init__(self , Value , nex_node = None ):
        self.Value = Value
        self.next_node = nex_node
        self.prev_node = nex_node
        
class CircularDeLinkedList : 
    
    def __init__(self , datatype = int):
        self.Tail = None
        self.datatype = datatype
        
    def __str__(self):
        if self.Tail.next_node is None :
            return  str(self.Tail.Value)
        temp_node = self.Tail.next_node
        result = ""
        while temp_node and temp_node is not self.Tail:
            result += str(temp_node.Value)
            if temp_node.next_node is not None :
                result += " <--> "
            temp_node = temp_node.next_node
            
        result += str(temp_node.Value)
        return result
    
    def Get(self , value):
        
        if self.Tail.Value == value :
            return self.Tail
        
        current = self.Tail.next_node
        
        while current is not self.Tail :
            if current.Value == value : return current
            current = current.next_node
    
    def Insert(self , value):
        if not isinstance(value , self.datatype):
            raise TypeError(f"linkedList only accepts data of type :{self.datatype}!")
        
        node = Node(value)
        
        if self.Tail is None :
            self.Tail = node
            return
        
        if self.Tail.next_node is None :
            self.Tail.next_node = node
            self.Tail.prev_node = node
            node.next_node = self.Tail
            node.prev_node = self.Tail
            self.Tail = node
            return
        
        node.next_node = self.Tail.next_node
        node.prev_node = self.Tail
        self.Tail.next_node = node
        node.next_node.prev_node = node
        
        self.Tail = node
        
    def Delete(self , Node):
        if Node is None :
            raise ValueError("Node is null!")
        
        head =  self.Tail
        
        if Node is self.Tail :
            self.Tail.prev_node.next_node = self.Tail.next_node
            self.Tail.next_node.prev_node = self.Tail.prev_node
            self.Tail = self.Tail.prev_node
                
        while head.next_node is not Node or head.next_node is self.Tail :
            head = head.next_node
            
        if head.next_node is self.Tail :
            raise ValueError(f'Node : {Node} not found in the linked list !')
        
        head.next_node = head.next_node.next_node
        head.next_node.next_node.prev_node = head
        
LL = CircularDeLinkedList(float)

LL.Insert(5.0)
print(LL)
LL.Insert(6.0)
print(LL)
LL.Insert(7.0)
print(LL)    

LL.Delete(LL.Get(6.0))
print(LL)