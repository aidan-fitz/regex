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
        # A tuple is hashable if and only if all of its elements are hashable. So this tuple can be added to a set.
        # Using modulo to keep the to_index within range (list indexing takes care of from_index automatically).
        self.edges[from_index].add( (to_index % len(self.vertices), label) )

    '''
    Returns the outdegree of the vertex (the number of edges leading from the vertex).
    '''
    def outdegree(self, index):
        return len(self.edges[from_index])

    '''
    Returns the indegree of the vertex (the number of edges leading to the vertex).
    '''
    def indegree(self, index):
        pass

    '''
    Appends a graph to this graph, adding a directed edge from the from_index'th vertex of this graph to the to_index'th vertex of the other graph.
    '''
    def append(self, graph, from_index, to_index=0, label=None):
        augend = len(self.vertices)
        self.vertices += graph.vertices
        for src_from_index in range(len(graph.edges)):
            for src_to_index, label in graph.edges[i]:
                self.add_edge(src_from_index + augend, src_to_index + augend, label)
        self.add_edge(from_index, to_index + augend, label)

    '''
    Returns the value of the index'th vertex.
    '''
    def vertex(self, index):
        return self.vertices[index]

    '''
    Returns the index of the first vertex having the given value.
    '''
    def index(self, value):
        return self.vertices.index(value)
