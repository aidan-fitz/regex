class DirectedGraph:
    '''
    Initializes an empty graph.
    '''
    def __init__(self):
        self.vertices = []
        self.edges = []

    '''
    Adds a new vertex to the graph, initializes it with an empty set of edges, and returns the index of the vertex.
    '''
    def add_vertex(self, value=None):
        index = len(vertices)
        self.vertices.append(value)
        self.edges.append(set())
        return index

    '''
    Sets the value of the vertex to the given value.
    If -|V| <= index < 0, then the index of the vertex modified will be index + |V|.
    '''
    def set_vertex(self, index, value=None):
        self.vertices[index] = value

    '''
    Adds a directed edge from vertex from_index to vertex to_index.
    The label, if any, must be hashable (i.e. have a __hash__(self) method).
    '''
    def add_edge(self, from_index, to_index, label=None):
        self.edges[from_index].add( (to_index % len(self.vertices), label) )

    '''
    Returns the degree of the vertex (the number of edges leading from the vertex).
    '''
    def degree(self, index):
        return len(self.edges[from_index])
