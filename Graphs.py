#Breadth First Traversal for a Graph


from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Breadth First Traversal (starting from node 2):")
    g.bfs(2)

# Depth First Traversal for a Graph

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Depth First Traversal (starting from node 2):")
    g.dfs(2)

# Count the number of nodes at given level in a tree using BFS

from collections import defaultdict, deque

class Tree:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, parent, child):
        self.graph[parent].append(child)

    def count_nodes_at_level(self, start_node, target_level):
        if start_node not in self.graph:
            return 0

        queue = deque([(start_node, 0)])
        count = 0

        while queue:
            node, level = queue.popleft()

            if level == target_level:
                count += 1

            for neighbor in self.graph[node]:
                queue.append((neighbor, level + 1))

        return count

if __name__ == "__main__":
    t = Tree()
    t.add_edge(0, 1)
    t.add_edge(0, 2)
    t.add_edge(1, 3)
    t.add_edge(1, 4)
    t.add_edge(2, 5)
    t.add_edge(2, 6)

    target_level = 2
    start_node = 0
    result = t.count_nodes_at_level(start_node, target_level)

    print(f"Number of nodes at level {target_level} starting from node {start_node}: {result}")

# Count number of trees in a forest

from collections import defaultdict

class Forest:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, visited):
        visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def count_trees(self):
        visited = set()
        num_trees = 0

        for node in list(self.graph):
            if node not in visited:
                num_trees += 1
                self.dfs(node, visited)

        return num_trees

if __name__ == "__main__":
    f = Forest()
    f.add_edge(0, 1)
    f.add_edge(0, 2)
    f.add_edge(1, 3)
    f.add_edge(4, 5)

    num_trees = f.count_trees()
    print("Number of trees in the forest:", num_trees)

# Detect Cycle in a Directed Graph

from collections import defaultdict

class DirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[node] = False
        return False

    def is_cyclic(self):
        visited = [False] * len(self.graph)
        rec_stack = [False] * len(self.graph)

        for node in range(len(self.graph)):
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True

        return False

if __name__ == "__main__":
    g = DirectedGraph()
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)

    if g.is_cyclic():
        print("The graph contains a cycle.")
    else:
        print("The graph does not contain a cycle.")
