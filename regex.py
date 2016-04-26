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

    def transition(self, state, char):
        # 0. Initialize a set of empty string transition destinations
        empty = set()
        # 1. Test all the non-empty string transitions
        #print(self.graph.edges[state])
        for dest, label in self.graph.edges[state]:
            #print(char)
            #print(label)
            if char == label or char in label:
                return dest
            elif label == '':
                empty.add(dest)
            else:
                #print('Not found')
                return -1
        # 2. Test all the empty string transitions
        else:
            destinations = [self.transition(dest, char) for dest in empty if dest >= 0]
            return destinations[0] if len(destinations) > 0 else -1

    def match(self, string):
        state = 0
        strindex = 0
        # Negative state number means we've left the graph
        while strindex < len(string):
            char = string[strindex]
            #print('state %d' % state)
            next_state = self.transition(state, char)
            if next_state < 0:
                break
            else:
                state = next_state
                strindex += 1
        return self.graph.vertex(state)

# Coding the graph manually
regex = Regex('ab*')
regex.graph.add_vertex(False)
regex.graph.add_vertex(True)
regex.graph.add_edge(0, 1, 'a')
regex.graph.add_edge(1, 1, 'b')

print('state 0: ' + str(regex.graph.vertex(0)))
print('state 1: ' + str(regex.graph.vertex(1)))

print(regex.match('abbbbb'))
print(regex.match('c'))
print(regex.match('cab'))
