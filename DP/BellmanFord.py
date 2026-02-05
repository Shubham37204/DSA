import sys

class Edge:
    def __init__(self, v, wt):
        self.v = v
        self.wt = wt

def bellman_ford(src, g, V):
    dist = [sys.maxsize] * V
    dist[src] = 0

    # V-1 relaxations
    for _ in range(V - 1):
        for u in range(V):
            for e in g[u]:
                if dist[u] != sys.maxsize and dist[e.v] > dist[u] + e.wt:
                    dist[e.v] = dist[u] + e.wt

    # print result
    for d in dist:
        print(d, end=" ")
    print()


def main():
    V = 5
    g = [[] for _ in range(V)]   # vector<vector<Edge>> g(V)

    g[0].append(Edge(1, 2))
    g[0].append(Edge(2, 4))

    g[1].append(Edge(4, -1))
    g[1].append(Edge(2, -4))

    g[2].append(Edge(3, 2))

    g[3].append(Edge(4, 4))

    src = 0
    bellman_ford(src, g, V)


if __name__ == "__main__":
    main()
