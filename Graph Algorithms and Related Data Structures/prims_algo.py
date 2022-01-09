from collections import defaultdict
from heapq import *

"""
PRIMS ALGORITHM IS IMPLEMENTED IN THE BELOW FUNCTION 
WHICH IS USED TO CONSTRUCT THE MINIMUM SPANNING TREE
"""
def Algorithm_prims( nodes, edges ):
    vertices = defaultdict( list )
    minimum_spanning_tree = []
    for a1,a2,curr in edges:
        vertices[ a2 ].append( (curr, a2, a1) )
        vertices[ a1 ].append( (curr, a1, a2) )
    not_visited = vertices[ nodes[0] ][:]
    used = set( nodes[ 0 ] )
    heapify( not_visited )
    while not_visited:
        path_cost, a1, a2 = heappop( not_visited )
        if a2 not in used:
            used.add( a2 )
            minimum_spanning_tree.append( ( a1, a2, path_cost ) )
            for _ in vertices[ a2 ]:
                if _[ 2 ] not in used:
                    heappush( not_visited, _ )
    return minimum_spanning_tree