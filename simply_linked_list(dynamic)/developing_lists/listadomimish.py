class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Creating an list
linked_list = LinkedList()

# Adding elements
linked_list.append(1)
linked_list.append(5)
linked_list.append(9)
linked_list.append(13)
linked_list.append(27)
linked_list.append(89)

# Displaying the linked list
linked_list.display()
