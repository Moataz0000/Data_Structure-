
"""
A good thing about Linked Lists is that when inserting or removing a node, other elements do not have to be  in memory.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse(head):
    """Go through the linked list by following the links from one node to the next"""
    current_node = head
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print(None)


def find_lowest_value(head):
    min_value = head.data
    current_node = head.next

    while current_node:
        if current_node.data < min_value:
            min_value = current_node.data
        current_node = current_node.next 
    return min_value


def delete_node(head, node):
    if head == node:
        return head.next 
    
    current_node = head
    while current_node.next and current_node.next != node:
        current_node = current_node.next 

    if current_node.next is None:
        return head
    
    current_node.next = current_node.next.next

    return head


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(0)

node1.next = node2
node2.next = node3
node3.next = node4


traverse(node1)
# print(f'The lowest value in the linked list is: {find_lowest_value(node1)}')

# delete node 4
delete_node(node1, node4)
delete_node(node1, node3)

traverse(node1)
