# we are focusing on pop method
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def append(self, value):
        new_node = Node(value)
        last_node = self.tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            last_node.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        empty_linked_list = self.head == None # the first edge case where list is already empty
        one_node_list = self.length == 1 and self.head == self.tail # second  case where list contain 1 item 
        if empty_linked_list:
            return None
        elif one_node_list:
            node_to_return = self.head
            # just point both head and tail to none
            self.head = None 
            self.tail = None
            self.length -=1
            return node_to_return
        else:
            # we will have 2 poitners pointing to the head the begining
            prev_node = self.head
            current_node = self.head
            while current_node is not self.tail: # here we need 2 pointers 1 for the node before the last node and one for the last node
                prev_node = current_node
                current_node = current_node.next
            self.tail = prev_node # pointing the tail to the node before the last node
            prev_node.next = None # pointing the pointer of the node before the last node to None 
            self.length -= 1 # decrymenting the length 
            return current_node # returning the node we have poped 


my_linked_list = LinkedList(4)

my_linked_list.append(5)
my_linked_list.append(6)

my_linked_list.print_list()  # 4 , 5 and 6 will be returned

print("After Popping item")
my_linked_list.pop()
my_linked_list.print_list() # will give you 4 , 5 
