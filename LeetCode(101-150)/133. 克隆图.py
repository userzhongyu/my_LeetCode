"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.dfs(node, {})

    def dfs(self, node: Optional['Node'], exist: dict):
        if not node:
            return
        # 如果当前节点已经被复制，则返回复制的节点
        if node in exist:
            return exist[node]

        # 如果当前节点未被复制，则复制一个新的节点
        clone = Node(node.val, [])

        # 创建哈希映射，将旧的节点与对应的复制节点映射起来
        exist[node] = clone

        # 遍历旧节点的 neighbors ，并将其放入复制节点的 neighbors 中
        for item in node.neighbors:
            clone.neighbors.append(self.dfs(item, exist))

        # 将新复制的节点返回
        return clone


def print_graph(node):
    """Helper function to print the graph in an adjacency list format."""
    visited = set()

    def dfs(node):
        if not node or node in visited:
            return
        visited.add(node)
        print(f"Node {node.val}: {[neighbor.val for neighbor in node.neighbors]}")
        for neighbor in node.neighbors:
            dfs(neighbor)

    dfs(node)


def build_graph(adj_list):
    """Builds a graph from an adjacency list."""
    if not adj_list:
        return None
    nodes = {i: Node(i) for i in range(1, len(adj_list) + 1)}
    for i, neighbors in enumerate(adj_list, start=1):
        nodes[i].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]  # Return the reference to the first node


# Example main function
def main():
    # Adjacency list of the input graph
    adj_list = [
        [2, 4],  # Node 1 is connected to Node 2 and Node 4
        [1, 3],  # Node 2 is connected to Node 1 and Node 3
        [2, 4],  # Node 3 is connected to Node 2 and Node 4
        [1, 3]  # Node 4 is connected to Node 1 and Node 3
    ]

    # Step 1: Build the graph
    original_graph = build_graph(adj_list)

    print("Original Graph:")
    print_graph(original_graph)

    # Step 2: Clone the graph
    cloned_graph = cloneGraph(original_graph)

    print("\nCloned Graph:")
    print_graph(cloned_graph)


# Replace `cloneGraph` with your implementation.
if __name__ == "__main__":
    main()
