class Node :
    def __init__(self , value , next = None , prev = None):
        self.Value = value
        self.next_node = next
        self.prev_node = prev
        
class DeLinkedList:
    def __init__(self , datatype = int ):
        self.Head = None
        self.datatype = datatype
        
    def __str__(self):
        
        resualt = ""
        if self.Head is None :
            return resualt
        
        current = self.Head
        
        while current is not None :
            resualt += str(current.Value)
            if current.next_node is not None :
                resualt += " <--> "
            current = current.next_node
        
        return resualt
   
    def Get(self , value):
        current = self.Head
        while current is not None:
            if current.Value == value:
                return current
            current = current.next_node
        raise ValueError(f'No node found with value {value}')
   
    def Insert(self, value):
        if not isinstance(value , self.datatype):
            raise TypeError(f"linkedList only accepts data of type :{self.datatype}!")
        
        node = Node(value)
        
        if self.Head is None:
            self.Head = node
            return

        current = self.Head
        while current.next_node is not None :
            current = current.next_node
        current.next_node = node
        node.prev_node = current
    
    def Delete(self , Node):
        if Node is None:
            raise ValueError('can not delete a null node')
        
        current = self.Head
        while current is not None :
            if current.Value == Node.Value:
                Node.prev_node.next_node = Node.next_node
                return
            current = current.next_node
        raise ValueError(f'node {Node} not found in the linked list !')

DELL = DeLinkedList(float)

print(DELL)

DELL.Insert(5.0)
print(DELL)
DELL.Insert(6.0)
print(DELL)
DELL.Insert(7.0)
print(DELL)

DELL.Delete(DELL.Get(6.0))

print(DELL)

