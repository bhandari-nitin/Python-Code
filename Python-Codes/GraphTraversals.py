#####################################################################
######## Graph , Adjacency List, Adjacencey Matrix, BFS, DFS ########
#####################################################################

# Class Vertex to form a new vertex
class Vertex(object):
    def __init__(self, vertex_value):
        self.value = vertex_value                                   # Index of the vertex
        self.edges = []
        self.visited = False

# Class Edge to form a new edge
class Edge(object):
    def __init__(self, edge_val, vertex_from, vertex_to):
        self.value = edge_val                                       # weight of the edge
        self.vertex_from = vertex_from
        self.vertex_to = vertex_to

# Class Graph for adjcenecy list, adjcenecy matrix and graph traversals (BFS and DFS)
class Graph(object):
    def __init__(self, vertices=[], edges=[]):
        self.vertices = vertices
        self.edges = edges
        self.vertex_names = []                                      # List that has the names of the vertices
        self._node_map = {}                                         # Dictionary that maps vertex values to vertices(address)

    def set_vertex_names(self, names):
        self.vertex_names = list(names)                             # Maps vertex values to their names 

    def insert_vertex(self, new_vertex_val):
        new_vertex = Vertex(new_vertex_val)
        self.vertices.append(new_vertex)
        self._node_map[new_vertex_val] = new_vertex                 # Maps vertex values(key) to vertices(address)(value)
        return new_vertex

    def insert_edge(self, new_edge_val, vertex_from_val, vertex_to_val):
        edge_vertices = {vertex_from_val:None, vertex_to_val:None}  # Dictionary that maps values of verticies of an edge to their vertex
        for vertex in self.vertices:                                # Vertices of the graph
            if vertex.value in edge_vertices:                       # Checks for the keys(Vertex Values) in the edge-vertices dictonary 
                edge_vertices[vertex.value] = vertex
                if all(edge_vertices.values()):
                    break
        for vertex_val in edge_vertices:                            # If the vertices in the edge_vertices does not exists, create new vertices 
            edge_vertices[vertex_val] = edge_vertices[vertex_val] \
                                        or self.insert_vertex(vertex_val) #?

        vertex_from = edge_vertices[vertex_from_val]
        vertex_to = edge_vertices[vertex_to_val]
        new_edge = Edge(new_edge_val, vertex_from, vertex_to)
        vertex_from.edges.append(new_edge)                          #?
        vertex_to.edges.append(new_edge)                            #?
        self.edges.append(new_edge)

    def get_edge_list(self):
        return [(e.value, e.vertex_from, e.vertex_to) for e in self.edges]

    def get_edge_list_names(self):
        return[(e.value, self.vertex_names[e.vertex_from.value], \
                self.vertex_names[e.vertex_to.value]) for e in self.edges]

    def find_max_index(self):                                       #Return the highest found node number Or the length of the node names if set with set_node_names().
        if len(self.vertex_names)>0:        
            return len(self.vertex_names)
        max_index = -1
        if len(self.vertcies):
            for vertex in self.vertices:
                if vertex.value > max_index:
                    max_index = vertex.value
                    return max_index

    def get_adj_list(self):                                         #Return a list of lists. The indices of the outer list represent "from" nodes.
        max_index = self.find_max_index()
        adj_list = [[] for _ in range(max_index)]                   #Edge-from is used as index in the adj list consiting of another list with list with tuples (Edge-to, edge_value)     
        for e in self.edges:
            from_value, to_value = e.vertex_from.value, e.vertex_to.value
            adj_list[from_value].append((to_value, e.value))
        return [a or None for a in adj_list]

    def get_adj_list_names(self):                                   #?
        adj_list = self.get_adj_list()

        def convert_to_names(pair, graph=self):                     #?
            vertex_number, value = pair
            return (graph.vertex_names[vertex_number], value)

        def map_conversion(adj_list_for_vertex):                    #?
            if adj_list_for_vertex is None:
                return None
            return map(convert_to_names, adj_list_for_vertex)
        return [map_conversion(adj_list_for_vertex) \
                for adj_list_for_vertex in adj_list]

    def get_adj_matrix(self):
        max_index = self.find_max_index()
        adj_matrix = [[0] * (max_index) for _ in range(max_index)]
        for e in self.edges:
               from_index, to_index = e.vertex_from.value, e.vertex_to.value
               adj_matrix[from_index][to_index] = e.value
        return adj_matrix

    def find_vertex(self, vertex_value):
        #Return the node with the value of vertex number or none
        return self._node_map.get(vertex_value)                    # get function is applied on dictionary '_node_map' to get the address of the vertex

    def _clear_visited(self):
        for v in self.vertices:
            v.visited = False

    def dfs_helper(self, start_vertex):
        ret_list = [start_vertex.value]
        start_vertex.visited = True
        edges_out = [e for e in start_vertex.edges if e.vertex_to.value != start_vertex.value]
        for edge in edges_out:
            if not edge.vertex_to.visited:
                ret_list.extend(self.dfs_helper(edge.vertex_to))
        return ret_list

    def dfs(self, start_vertex_num):
        self._clear_visited()
        start_vertex = self.find_vertex(start_vertex_num)
        return self.dfs_helper(start_vertex)

    def dfs_names(self, start_vertex_num):
        return[self.vertex_names[num] for num in self.dfs(start_vertex_num)]

    def bfs(self, start_vertex_num):
        vertex = self.find_vertex(start_vertex_num)
        self._clear_visited()
        ret_list = []
        queue = [vertex]
        vertex.visited = True
        def enqueue(n, q=queue):
            n.visited = True
            q.append(n)
        def unvisited_outgoing_edge(n, e):
            return ((e.vertex_from.value == n.value) and
                    (not e.vertex_to.visited))
        while queue:
            vertex = queue.pop(0)
            ret_list.append(vertex.value)
            for e in vertex.edges:                              # Vertex has attribute list edges
                if unvisited_outgoing_edge(vertex, e):
                    enqueue(e.vertex_to)
        return ret_list

    def bfs_names(self, start_vertex_num):
        return [self.vertex_names[num] for num in self.bfs(start_vertex_num)]

# Main function to access Graph and it's functions using it's objects
if __name__ == '__main__':
    graph = Graph()
    graph.set_vertex_names(('Mountain View',    #0
                        'San Francisco',        #1
                        'London',               #2
                        'Shangai',              #3
                        'Berlin',               #4
                        'Sao Paolo',            #5
                        'Bangalore'))           #6

    graph.insert_edge(51, 0, 1)     # MV <-> SF
    graph.insert_edge(51, 1, 0)     # SF <-> MV
    graph.insert_edge(9950, 0, 3)   # MV <-> Shanghai
    graph.insert_edge(9950, 3, 0)   # Shanghai <-> MV
    graph.insert_edge(10375, 0, 5)  # MV <-> Sao Paolo
    graph.insert_edge(10375, 5, 0)  # Sao Paolo <-> MV
    graph.insert_edge(9900, 1, 3)   # SF <-> Shanghai
    graph.insert_edge(9900, 3, 1)   # Shanghai <-> SF
    graph.insert_edge(9130, 1, 4)   # SF <-> Berlin
    graph.insert_edge(9130, 4, 1)   # Berlin <-> SF
    graph.insert_edge(9217, 2, 3)   # London <-> Shanghai
    graph.insert_edge(9217, 3, 2)   # Shanghai <-> London   
    graph.insert_edge(932, 2, 4)    # London <-> Berlin
    graph.insert_edge(932, 4, 2)    # Berlin <-> London
    graph.insert_edge(9471, 2, 5)   # London <-> Sao Paolo
    graph.insert_edge(9471, 5, 2)   # Sao Paolo <-> London
    # (6) 'Bangalore' is intentionally disconnected (no edges)
    # for this problem and should produce None in the
    # Adjacency List, etc.

    import pprint
    pp = pprint.PrettyPrinter(indent=2)

    print "Edge List"
    pp.pprint(graph.get_edge_list_names())

    print "\nAdjacency List"
    pp.pprint(graph.get_adj_list_names())

    print "\nAdjacency Matrix"
    pp.pprint(graph.get_adj_matrix())

    print "\nDepth First Search"
    pp.pprint(graph.dfs_names(2))

    # Should print:
    # Depth First Search
    # ['London', 'Shanghai', 'Mountain View', 'San Francisco', 'Berlin', 'Sao Paolo']

    print "\nBreadth First Search"
    pp.pprint(graph.bfs_names(2))
    # test error reporting
    # pp.pprint(['Sao Paolo', 'Mountain View', 'San Francisco', 'London', 'Shanghai', 'Berlin'])

    # Should print:
    # Breadth First Search
    # ['London', 'Shanghai', 'Berlin', 'Sao Paolo', 'Mountain View', 'San Francisco'] 
















              
