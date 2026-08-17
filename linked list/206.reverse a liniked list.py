class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def reverse(self):
        prev = None
        temp = self.head
        while temp:
            front = temp.next   # save next node before we overwrite temp.next
            temp.next = prev    # reverse the pointer
            prev = temp         # move prev forward
            temp = front        # move temp forward
        self.head = prev        # prev is the new head after loop ends

    def display(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.data))
            current = current.next
        print(" -> ".join(values) if values else "empty list")


# --- testing it ---
ll = linkedlist()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

print("Before reverse:")
ll.display()

ll.reverse()

print("After reverse:")
ll.display()