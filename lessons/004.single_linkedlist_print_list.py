# we are focusing on print method 
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

    def print_list(self):
        current_node = self.head # define starting node
        while current_node is not None:
            print(current_node.value) # print the value of node i am currently standing on 
            current_node = current_node.next # reassign the node value to the next node in order for the loop to work


my_linked_list = LinkedList(4)


my_linked_list.print_list()