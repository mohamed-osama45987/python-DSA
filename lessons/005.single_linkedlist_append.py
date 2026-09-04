# we are focusing on append method
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

    # adds a value as a node at the end of the list
    def append(self, value):
        new_node = Node(value)
        last_node = self.tail
        # edge case where list does not contain any node so head and tail will point the same node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            last_node.next = new_node  # pointing the last node pointer to the new node
            self.tail = new_node  # pointing the tail to the new node
        self.length += 1
        return True


my_linked_list = LinkedList(4)

my_linked_list.append(5)
my_linked_list.append(6)

my_linked_list.print_list() # 4 , 5 and 6 will be returned 
