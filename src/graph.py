class Edge: 
    def __init__(self, destination):
        self.destination = destination

class Vertex: 
    def __init__(self, value, **pos): #TODO: Test default arguments
        self.value = value
        self.color = 'white'
        self.pos = pos
        self.edges = []

class Graph:
    def __init__(self):
        self.vertexes = []

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('t1', x=40, y=40)
        debug_vertex_2 = Vertex('t2', x=140, y=140)
        debug_vertex_3 = Vertex('t3', x=160, y=200)
        debug_vertex_4 = Vertex('t4', x=340, y=340)
        debug_vertex_5 = Vertex('t5', x=200, y=250)
        debug_vertex_6 = Vertex('t6', x=360, y=250)





        debug_edge_1 = Edge(debug_vertex_2)
        debug_vertex_1.edges.append(debug_edge_1)

        debug_edge_2 = Edge(debug_vertex_3)
        debug_vertex_2.edges.append(debug_edge_2)

        debug_edge_3 = Edge(debug_vertex_4)
        debug_vertex_3.edges.append(debug_edge_3)

        debug_edge_4 = Edge(debug_vertex_5)
        debug_vertex_4.edges.append(debug_edge_4)

        debug_edge_5 = Edge(debug_vertex_6)
        debug_vertex_5.edges.append(debug_edge_5)



        self.vertexes.extend([debug_vertex_1, debug_vertex_2])
        self.vertexes.extend([debug_vertex_3, debug_vertex_4])
        self.vertexes.extend([debug_vertex_5, debug_vertex_6])
        
