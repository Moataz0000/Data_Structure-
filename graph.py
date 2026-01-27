from typing import Any
from collections import deque

class Graph:
    def __init__(self):
        self.adj_list: dict = {}
    

    def add_node(self, node: Any) -> bool:
        """Adds a new node to the graph."""
        if node not in self.adj_list:
            self.adj_list[node] = []
            return True
        return False
    
    def add_edge(self, node1: Any, node2: Any) -> bool:
        """Creates a connection between two nodes."""
        if node1 in self.adj_list and node2 in self.adj_list:
            self.adj_list[node1].append(node2)
            self.adj_list[node2].append(node1)
            return True
        return False
    

    def display(self) -> None:
        """Shows the graph structure."""
        for node, neighbors in self.adj_list.items():
            print(f"{node}: {neighbors}")


    def bfs(self, start_node: Any):
        if start_node not in self.adj_list:
            print("Start node not found!")
            return 
        
        visited: set = set()
        queue: deque = deque([start_node])
        visited.add(start_node)

        print(f"BFS starting from {start_node}:", end=" ")

        while queue:
            current_node = queue.popleft()
            print(current_node, end=" ")
        for neighbor in self.adj_list[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        print()
    

graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")

graph.bfs("A") 
# Output: BFS starting from A: A B C D