from collections import defaultdict
from heapq import *

def dijkstra_undirected(edges, source,destination):
    graph = defaultdict(list)
    for a,b,c in edges:
        graph[a].append((c,b))
    start, visited, mins = [(0,source,())], set(), {source: 0}
    while start:
        (path_cost,vertex1,path) = heappop(start)
        if vertex1 not in visited:
            visited.add(vertex1)
            path = (vertex1, path)
            # print(vertex1,path)
            visited.add(vertex1)
            if vertex1 == destination: 
                return ( path_cost, path )
            for _ , vertex2 in graph.get(vertex1, ()):
                if vertex2 in visited: 
                    continue
                previous_node = mins.get(vertex2, None)
                next_node = path_cost + int( _ )
                if previous_node is None or next_node < previous_node:
                    mins[vertex2] = next_node
                    heappush(start, (next_node, vertex2, path))
    return (dijkstra_undirected(edges,destination,source))