class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the head (the first node)
        newHeadNode = Node(value)
        newHeadNode.next = self.head
        self.head = newHeadNode

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        counter = 0
        while node.next:
            counter += 1
            node = node.next
        node.next = Node(value)
        return

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        if self.head is None:
            return None
        
        node = self.head
        
        while node:
            if node.value == value:
                return node
            node = node.next
        
        return node
    
    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head == None:
            return
        elif self.head.value == value:
            node = self.head
            self.head = node.next
            node.next = self.head
            return
        else:
            node = self.head
            while node.next:
                if node.next.value == value:
                    node.next = node.next.next
                    return
                node = node.next

    
    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head == None:
            return None
        node = self.head
        item = node.value
        self.head = node.next
        node.next = self.head
        return item
        
    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        if self.head == None or pos == 0:
            self.prepend(value)
            return
        elif pos > self.size():
            self.append(value)
            return
        counter = 0
        node = self.head
        while (counter + 1) < pos:
            node = node.next
            counter += 1
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
        return
    
    def size(self):
        """ Return the size or length of the linked list. """
        if self.head is None:
            return 0
        node = self.head
        counter = 0
        while node.next:
            counter += 1
            node = node.next
        return counter+1

    def to_list(self):
        if self.head is None:
            return None
        python_list = []
        node = self.head
        while node:
            python_list.append(node.value)
            node = node.next
        return python_list

def print_linked_list(head):
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next

def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    if len(input_list) == 0:
        return None
    elif len(input_list) == 1:
        head = Node(input_list[0])
        return head
    else:
        temp_node = Node(input_list[0])
        head = temp_node
        for i in range(len(input_list)-1):
            temp_node.next = Node(input_list[i+1])
            temp_node = temp_node.next
        return head

def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    new_list = LinkedList()
    node = linked_list.head
    prev_node = None

    # A bit of a complex operation here. We want to take the
    # node from the original linked list and prepend it to 
    # the new linked list
    for value in linked_list:
        new_node = Node(value)
        new_node.next = prev_node
        prev_node = new_node
    new_list.head = prev_node
    return new_list
    
## Test your implementation here

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
    
# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"        
# print(linked_list.to_list())

llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

flipped = reverse(llist)
is_correct = list(flipped) == list([0,-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")
# input_list = [1, 2, 3, 4, 5, 6]
# head = create_linked_list(input_list)
# test_function(input_list, head)

# input_list = [1]
# head = create_linked_list(input_list)
# test_function(input_list, head)

# input_list = []
# head = create_linked_list(input_list)
# test_function(input_list, head)


# # Solution

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def prepend(self, value):
#         """ Prepend a node to the beginning of the list """

#         if self.head is None:
#             self.head = Node(value)
#             return

#         new_head = Node(value)
#         new_head.next = self.head
#         self.head = new_head

#     def append(self, value):
#         """ Append a node to the end of the list """
#         # Here I'm not keeping track of the tail. It's possible to store the tail
#         # as well as the head, which makes appending like this an O(1) operation.
#         # Otherwise, it's an O(N) operation as you have to iterate through the
#         # entire list to add a new tail.

#         if self.head is None:
#             self.head = Node(value)
#             return

#         node = self.head
#         while node.next:
#             node = node.next

#         node.next = Node(value)

#     def search(self, value):
#         """ Search the linked list for a node with the requested value and return the node. """
#         if self.head is None:
#             return None

#         node = self.head
#         while node:
#             if node.value == value:
#                 return node
#             node = node.next

#         raise ValueError("Value not found in the list.")


#     def remove(self, value):
#         """ Delete the first node with the desired data. """
#         if self.head is None:
#             return

#         if self.head.value == value:
#             self.head = self.head.next
#             return

#         node = self.head
#         while node.next:
#             if node.next.value == value:
#                 node.next = node.next.next
#                 return
#             node = node.next

#         raise ValueError("Value not found in the list.")


#     def pop(self):
#         """ Return the first node's value and remove it from the list. """
#         if self.head is None:
#             return None

#         node = self.head
#         self.head = self.head.next

#         return node.value

#     def insert(self, value, pos):
#         """ Insert value at pos position in the list. If pos is larger than the
#             length of the list, append to the end of the list. """
#         if pos == 0:
#             self.prepend(value)
#             return

#         index = 0
#         node = self.head
#         while node.next and index <= pos:
#             if (pos - 1) == index:
#                 new_node = Node(value)
#                 new_node.next = node.next
#                 node.next = new_node
#                 return

#             index += 1
#             node = node.next
#         else:
#             self.append(value)

#     def size(self):
#         """ Return the size or length of the linked list. """
#         size = 0
#         node = self.head
#         while node:
#             size += 1
#             node = node.next

#         return size

#     def to_list(self):
#         out = []
#         node = self.head
#         while node:
#             out.append(node.value)
#             node = node.next
#         return out
