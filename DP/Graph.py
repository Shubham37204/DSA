class Graph:
    def __init__(self, V):
        self.V = V
        self.l = [[] for _ in range(V)]  # adjacency list

    def add_edge(self, u, v):
        # undirected graph
        self.l[u].append(v)
        self.l[v].append(u)

    # -------- DFS (Recursive) --------
    def dfs(self, u, visited):
        print(u, end=" ")
        visited[u] = True

        for v in self.l[u]:
            if not visited[v]:
                self.dfs(v, visited)

    # -------- BFS (Using basic list) --------
    def bfs(self, start):
        visited = [False] * self.V
        queue = []

        queue.append(start)
        visited[start] = True

        while len(queue) > 0:
            u = queue.pop(0)
            print(u, end=" ")

            for v in self.l[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)


def main():
    g = Graph(5)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 4)
    g.add_edge(1, 3)

    print("DFS Traversal:")
    visited = [False] * 5
    g.dfs(0, visited)

    print("\n\nBFS Traversal:")
    g.bfs(0)


if __name__ == "__main__":
    main()
