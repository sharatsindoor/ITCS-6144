from collections import deque, namedtuple
"""INITIALIZING ALL THE VERTICES WITH THE COST AS INFINITY."""
edge = namedtuple('edge', 'start, end, cost')
intial_values = float('inf')
def make_edge(start, end, cost=1):
    return edge(start, end, cost)

class Graph:
    """
    THIS CONSTRUCTOR IS USED TO INTIALSE THE GRAPH WITH THE BASIC VALUES.
    """
    def __init__(self, edges):
        not_correct_edges = [_ for _ in edges if len(_) not in [2, 3]]
        if not_correct_edges:
            raise ValueError('EDGES ARE IN WRONG FORMAT: {}'.format(not_correct_edges))
        self.edges = [make_edge(*_) for _ in edges]
    
    """
    IMPLEMENTING THE DIJSTRA'S ALGORITHM
    FOR THE DIRECTED GRAPH
    """
    def implementing_dijkstra_algorithm(self, start, destination):
        global path_cost
        assert start in self.vertices, 'THERE IS NO SUCH START NODE IN THE GRAPH'
        path_cost = {_: intial_values for _ in self.vertices}
        previous_node = {
        _: None for _ in self.vertices
        }
        path_cost[start] = 0
        vertex_all = self.vertices.copy()
        while vertex_all:
            present_node = min(
                vertex_all, key=lambda vertex: path_cost[vertex])
            vertex_all.remove(present_node)
            if path_cost[present_node] == intial_values:
                break   
            for adjacent_node, cost_per in self.neighbours[present_node]:
                alternate_path = path_cost[present_node] + int(cost_per)
                if alternate_path < path_cost[adjacent_node]:
                    path_cost[adjacent_node] = alternate_path
                    previous_node[adjacent_node] = present_node
        path, present_node = deque(), destination
        while previous_node[present_node] is not None:
            path.appendleft(present_node)
            present_node = previous_node[present_node]
        if path:
            path.appendleft(present_node)
        return path,path_cost
    """
    THIS IS FUNCTION IS USED TO CREATE THE CONNECTION BETWEEN THE TWO VERTICES
    """            
    def create_connection_vertices(self, vertex1, vertex2, path_cost=1, both_ends=True):
        node_pairs = self.getter_adjacent_nodes(vertex1, vertex2, both_ends)
        for _ in self.edges:
            if [_.start, _.end] in node_pairs:
                return ValueError(' EDGE FROM {} TO {} ALREADY EXISTS'.format(vertex1, vertex2))
            self.edges.append(_(start=vertex1, end=vertex2, cost=path_cost))
            if both_ends:
                self.edges.append(_(start=vertex2, end=vertex1, cost=path_cost))
    
    """
    THIS TWO ARE THE PROPERTIES FOR THE GRAPH
    -->WHERE THE VERICES REPRESENT THE EACH VERTEX PRESENT IN THE
    GRAPH.
    -->AND THE NEIGHBOURS IS USED TO FIND THE ADJACENT NODE IN THE GRAPH.
    """
    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))
        return neighbours
    @property
    def vertices(self):
        return set(
                sum(
            ([_.start, _.end] for _ in self.edges), []) )
    
    """
    HIS FUNCTION IS USED TO GET THE VERTICES 
    THAT CONNECTED OR THERE IS CONNECTION BETWEEN VERTICE 
    """
    def getter_adjacent_nodes(self, vertex1, vertex2, bidirectional=True):
        if bidirectional:
            adjacent_nodes= [[vertex1, vertex2], [vertex2, vertex1]]
        else:
            adjacent_nodes = [[vertex1, vertex2]]
        return adjacent_nodes
    """
    THIS FUNCTION IS USED TO REMOVE THE EDGES FROM THE GIVEN GRAPH
    IF THERE IS AN ALTERNATE PATH THAT IS USED TO CONNECT THE VERTEX WITH LESSER COST
    """    
    def delete_edge(self, vertex1, vertex2, bi_directionnal=True):
        adjacent_nodes = self.getter_adjacent_nodes(vertex1, vertex2, bi_directionnal)
        edges = self.edges[:]
        for _ in edges:
            if [_.start, _.end] in adjacent_nodes:
                self.edges.remove(_)
   
        
   