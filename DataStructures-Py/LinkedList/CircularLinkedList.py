class Node :
    def __init__(self , Value , nex_node = None ):
        self.Value = Value
        self.next_node = nex_node
        
        
class CircularLinkedList : 
    
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
                result += " -> "
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
            node.next_node = self.Tail
            self.Tail = node
            return
        
        node.next_node = self.Tail.next_node
        self.Tail.next_node = node
        self.Tail = node
    
    def Insert2(self , value , N : Node):
        if not isinstance(value , self.datatype):
            raise TypeError(f"linkedList only accepts data of type :{self.datatype}!")
        
        node = Node(value)
        
        node.next_node = N.next_node
        N.next_node = node
        
    def Delete(self , Node):
        if Node is None :
            raise ValueError("Node is null!")
        
        head =  self.Tail
        
        if Node is self.Tail :
            while head.next_node is not self.Tail:
                head = head.next_node
            head.next_node = head.next_node.next_node
            self.Tail = head
            return
                
        while head.next_node is not Node or head.next_node is self.Tail :
            head = head.next_node
            
        if head.next_node is self.Tail :
            raise ValueError(f'Node : {Node} not found in the linked list !')
        
        head.next_node = head.next_node.next_node
 
 
def detect_cycle(linked_list: CircularLinkedList) -> bool:
    slow_pointer = linked_list.Tail 
    fast_pointer = linked_list.Tail  

    while fast_pointer and fast_pointer.next_node:
        slow_pointer = slow_pointer.next_node     
        fast_pointer = fast_pointer.next_node.next_node   

        if slow_pointer == fast_pointer:
            return True

    return False
        
LL = CircularLinkedList(float)

LL.Insert(5.0)
print(LL)
LL.Insert(6.0)
print(LL)
LL.Insert(7.0)
print(LL)    

LL.Insert2(5.5 ,LL.Get(5.0))
print(LL)

LL.Delete(LL.Get(6.0))

print(LL)

print(detect_cycle(LL))