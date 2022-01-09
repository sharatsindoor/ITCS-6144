from prims_algo import Algorithm_prims
import time
"""
READING THE CONNECTIONS BETWEEN THE EDGES FROM THE " INPUT FILE" IN TEXT FORMAT.
"""
start=time.time()
input_file = open(r'Input4_UDGraph','r')
temp = []
vertices =[]
vertices_lable = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
vertices_lable =list(vertices_lable)
path_cost = 0
#READING THE DATA PRESENT THE GIVING
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
print(temp)
"""
IF THE GRAPH IS AN UNDIRECTED GRAPH.
"""
if(graph_type == 'U'):
    print("THE MINIMUM SPANNING TREE FOUND FOR AN UNDIRECTED GRAPH IS FOUND USING THE PRIM'S ALGORITHM")
    print("THE TOTAL NUMBER OF VERTICES:", total_vertices)
    print("THE TOTAL NUMBER OF EDGES :", total_edges)

for K in range(0,total_vertices):
    vertices.append(vertices_lable[K])

result= Algorithm_prims( vertices, edges )
l= 0

"""
PRINTING THE MINIMUM SPANNING TREE THAT HAS BEEN FORMED 
"""

if(graph_type == 'U'):
    graph="Undirected Graph"
else:
    graph = "Directed Graph"
print()
print("Printing th minimum spanning tree that has been formed for a "+graph)
for _ in result:
    print ("FROM:'{from_ver}' --> TO:'{to}' COST:: {path_cost}".format( from_ver = _[0], to = _[1], path_cost = _[2]))
    path_cost += int(result[l][2])
    l +=1
print("TOTAL PATH COST IS :: " ,path_cost)
end=time.time()
print("THE RUNNING TIME OF THE PRIMS ALGORITHM IS THAT",end-start,"seconds")