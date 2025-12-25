from typing import Any


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
    

graph = Graph()


graph.add_node("A")
graph.add_node("B")
graph.add_node("C")

graph.add_edge(node1="A", node2="B")
graph.add_edge(node1="B", node2="C")


graph.display()