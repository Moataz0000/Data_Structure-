
"""
A good thing about Linked Lists 
is that when inserting or 
removing a node, other elements 
do not have to be  in memory.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None




node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3


current_node = node1

while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.next
print("null")