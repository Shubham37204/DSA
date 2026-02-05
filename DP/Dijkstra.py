import heapq

class Edge:
    def __init__(self, v, wt):
        self.v = v
        self.wt = wt


def dijkstra(src, g, V):
    # distance array
    dist = [float('inf')] * V
    dist[src] = 0

    # min heap -> (distance, node)
    pq = []
    heapq.heappush(pq, (0, src))

    while len(pq) > 0:
        curr_dist, u = heapq.heappop(pq)

        # optional optimization
        if curr_dist > dist[u]:
            continue

        # edge relaxation
        for e in g[u]:
            if dist[e.v] > dist[u] + e.wt:
                dist[e.v] = dist[u] + e.wt
                heapq.heappush(pq, (dist[e.v], e.v))

    # print result
    for d in dist:
        print(d, end=" ")
    print()


def main():
    V = 6
    g = [[] for _ in range(V)]

    # same edges as your C++ main()
    g[0].append(Edge(1, 2))
    g[0].append(Edge(2, 4))

    g[1].append(Edge(2, 1))
    g[1].append(Edge(3, 7))

    g[2].append(Edge(4, 3))

    g[3].append(Edge(5, 1))

    g[4].append(Edge(3, 2))
    g[4].append(Edge(5, 5))

    # run dijkstra from source 0
    dijkstra(0, g, V)


if __name__ == "__main__":
    main()




# import heapq

# class Solution:
#     def dijkstra(self, V, adj, S):
#         # distance array
#         dist = [float('inf')] * V
#         dist[S] = 0

#         # min heap -> (distance, node)
#         pq = []
#         heapq.heappush(pq, (0, S))

#         while pq:
#             curr_dist, u = heapq.heappop(pq)

#             # optimization to skip outdated entries
#             if curr_dist > dist[u]:
#                 continue

#             # relax edges
#             for v, wt in adj[u]:
#                 if dist[v] > dist[u] + wt:
#                     dist[v] = dist[u] + wt
#                     heapq.heappush(pq, (dist[v], v))

#         return dist
