# first we make a node class to allow us to create nodes as all the methods in the linked
# list class needs first to create nodes
# remeber a node is just a dict with next and value properties {value : 7 , next: none }
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


my_linked_list = LinkedList(4) # intalizing a linked list object from the Linked list class

print(my_linked_list.head.value) # 4 