from dijkstra import Graph
from dijkstra_undirected import dijkstra_undirected
import time

def intialise(vertices_from_file):
    length_of_input= len(vertices_from_file)
    graph = vertices_from_file[1:length_of_input-1]
    total_edges = int(vertices_from_file[0][1])
    total_vertices =int( vertices_from_file[0][0])
    type_of_graph = str(vertices_from_file[0][2])
    return length_of_input,graph,total_edges,total_vertices,type_of_graph

if __name__ == "__main__":
    start =  time.time()
    l =[]
    input_file = open(r'Input_DGraph4','r')
    path_distance = ()
    vertices_from_file = []
    var =[]
    for _ in input_file.readlines():
        k=_.split()
        vertices_from_file.append(k)
    length_of_input,graph,total_edges,total_vertices,type_of_graph = intialise(vertices_from_file)
    if(type_of_graph == 'D'):
        for _ in range(1,total_edges+1):
            if(vertices_from_file[_][0] not in l):
                l.append(vertices_from_file[_][0])
        print("THE TOTAL NUMBER OF VERTICES::",total_vertices)
        print("THE TOTAL NUMBER OF EDGES::",total_edges)
        graph = Graph(graph)
        print("THE PATH FROM SOURCE(A) TO EVERY OTHER NODE IN THE DIRECTED GRAPH\n")
        for _ in range(1,len(l)):
            result=graph.implementing_dijkstra_algorithm("A",l[_])
            print(result[0])
        print ("THE SHORTEST PATH COST FROM A TO EVERY OTHER NODE IN THE DIRECTED GRAPH\n ")
        path_distance=result[1]
        print(path_distance)
        end=time.time()
        print("THE RUNNING TIME OF THE DIRECTED DIJKSTRA ALGORITHM",end-start,"seconds")
    
    """
    --------------------------------
    THIS IS FOR THE UNDIRECTED GRAPH
    -------------------------------- 
    """
    temp_list = []
    input_file = open(r'Input1_UDGraph','r')
    for _ in input_file.readlines():
        k=_.split()
        temp_list.append(k)
    var= []
    length_of_input,graph,total_edges,total_vertices,type_of_graph = intialise(temp_list)
    edges=temp_list[1:length_of_input-1]
    print("THE TOTAL NUMBER OF VERTICES:",total_vertices)
    print("THE TOTAL NUMBER OF EDGES:",total_edges)
    print ("DIJKSTRA'S UNDIRECTED GRAPH ALGORITHM")
    print("The path traversal is:")
    start = time.time()
    path = (dijkstra_undirected(edges, "A", "E"))
    #out2 = (dijkstra(edges, "A", "D"))
    print(path)
    end=time.time()
    print("THE RUNNING TIME OF THE UNDIRECTED DIJKSTRA ALGORITHM",end-start,"seconds")
        
    # for i in range (0,len(path) ):
    #     print(path[i])