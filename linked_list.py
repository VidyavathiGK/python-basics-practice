class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list data structure implementation."""
    
    def __init__(self):
        self.head = None

    def append(self, data) -> None:
        """Adds a new node with data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self) -> list:
        """Returns all elements in the linked list as a Python list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def delete_by_value(self, value) -> bool:
        """Deletes the first occurrence of a node containing the specified value."""
        current = self.head
        
        if current and current.data == value:
            self.head = current.next
            return True
            
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next
            
        if current is None:
            return False
            
        prev.next = current.next
        return True


# --- Example Usage ---
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    
    print("Linked List items:", ll.display())
    ll.delete_by_value(20)
    print("After deleting 20:", ll.display())
