from graph import DirectedGraph

class Regex:
    def __init__(self, regex):
        self.regex = regex
        # Vertices labelled with booleans, edges labelled with character classes (sets of zero or more characters)
        self.graph = DirectedGraph()
        self.compile()

    def compile(self):
        pass

    def match(self, string):
        pass
