from collections import defaultdict

class Graph:
    def __init__(self,vertex):
        self.V= vertex
        self.graph = defaultdict(list)
       
      
    """
    THIS FUNCTION IS USDE TO TRANSPOSE THE GRAPH INORDER TO 
    FIND WHETHER THE COMPONENTS OF THE GRAPH ARE STILL CONNECTED 
    SO THAT E CAN FIND THE STRONGLY CONNECTED COMPONENT OF THE GRAPH.
    """
    def transpose_of_graph(self):
        g = Graph(self.V)
        for _ in self.graph:
            for k in self.graph[_]:
                g.add_edge(k,_)
        return g

    """
    THIS FUNCTION IS FOR IMPLEMENTING THE DPETH-FIRST-SEARCH 
    WHICH IS USED TO FIND THE CONNECTED COMPONENT OF THE GRAPH.
    """
  
    def depth_first_search(self,v1,already_visited):
       
        already_visited[v1]= True
      
        print(chr(v1+65),end=" ")
        
       
        for _ in self.graph[v1]:
            if already_visited[_]==False:
              
                self.depth_first_search(_,already_visited)
        
       
  
   
    """
    THIS FUNCTION IS USED TO TAKE THE SOURCE VERTEX AND THE DESTINATION VERTEX
    (ANOTHER VERTEX) INORDER TO CREATE AN EDGE BETWEEN.
    """  
    def add_edge(self,u,v):
        self.graph[u].append(v)
   
        
    """
    THIS FUNCTION IS USED TO KEEP TRACK OF THE VERTICES THAT ARE BEING
    VISITED.
    """
    def vertices_visited_order(self,v1,already_visited, impl_stack):
        already_visited[v1]= True
        for i in self.graph[v1]:
            if already_visited[i]==False:
                self.vertices_visited_order(i, already_visited, impl_stack)
        impl_stack= impl_stack.append(v1)

    """
    THIS FUNCTIN IS USED TO FIND THE STRONGLY CONNECTED COMPONENT OF THE GRAPH
    WHERE THE GRAPH IS REVERSED TO FIND WHETHER THE CONNECTED COMPONENTS ARE STILL
    CONNECTED.AND THE CONNECTION IS DETECTED USING THE DEPTH-FIRST-SEARCH
    """
    def strongly_connected_graph(self):
        count=1
        already_traversed=[False]*(self.V)
        impl_stack = []
        for _ in range(self.V):
            if already_traversed[_]==False:
                self.vertices_visited_order(_, already_traversed, impl_stack)
        gr = self.transpose_of_graph()
        already_traversed =[False]*(self.V)
        while impl_stack:
             vertex= impl_stack.pop()
             if already_traversed[vertex]==False:
                print("THE STRONGLY CONNECTED COMPONENT",count)
                gr.depth_first_search(vertex, already_traversed)
                count+=1
                print()