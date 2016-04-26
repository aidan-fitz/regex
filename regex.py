from graph import DirectedGraph

def zero_or_one(graph):
    pass

def zero_or_more(graph):
    pass

def one_or_more(graph):
    pass

'''
A state machine that matches strings to a regular expression.
'''
class Regex:

    symbols = {
        '?': zero_or_one,
        '*': zero_or_more, # Kleene star
        '+': one_or_more
    }

    def __init__(self, regex):
        self.regex = regex
        # Vertices labelled with booleans, edges labelled with character classes (sets of zero or more characters)
        self.graph = DirectedGraph()
        self.compile()

    def compile(self):
        pass

    def match(self, string):
        state = 0
        strindex = 0
        # Negative state number means we've left the graph
        while state >= 0 and strindex < len(string):
            char = string[strindex]
            # TODO add support for empty string transitions
            empty_string_transitions = set()
            for dest, label in self.graph.edges:
                if char == label or char in label:
                    state = dest
                else:
                    state = -1
            strindex += 1
            pass
        return self.graph.vertex(state)
