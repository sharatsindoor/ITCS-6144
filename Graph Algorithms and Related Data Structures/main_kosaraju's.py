from kosaraju_graph import Graph
import time   
if __name__== "__main__":
    now = time.time()
    temp = []
    input_file = open(r'DirectedGraph_Input5','r')
    for _ in input_file.readlines():
        temp_var=_.split()
        temp.append(temp_var)
   
    """
    FROM THE INPUT GIVEN WE ARE FINDING THE NUMBER OF VERTICES PRESENT
    IN THE GIVEN GRAPH AND VERTICES AND THE EDGES PRESENT BETWEEN.
    """
    length = len(temp)
    total_vertices =int(temp[0][0])
    graph_type = str(temp[0][2])
    total_edges = int(temp[0][1])
    edges = temp[1:length-1]
    
    
    # Create a graph given in the above diagram
    g1 = Graph(total_vertices)
    for i in range(1,len(temp)):
        g1.add_edge((ord(temp[i][0])%65),(ord(temp[i][1])%65))
    print ("THE BELOW IS THE STRONGLY CONNECTED COMPONENT(VERTEX) OF THE GRAPH")
    g1.strongly_connected_graph()
    end=time.time()
    print("THE RUNNING TIME OF THE PROGRAM IS",end-now,"seconds")
