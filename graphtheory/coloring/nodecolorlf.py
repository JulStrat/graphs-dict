#!/usr/bin/python

class LargestFirstNodeColoring:
    """Find a largest first (LF) node coloring.
    
    Attributes
    ----------
    graph : input undirected graph or multigraph
    color : dict with nodes (values are colors)
    
    Notes
    -----
    Colors are 0, 1, 2, ...
    """

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict((node, None) for node in self.graph.iternodes())
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")

    def run(self):
        """Executable pseudocode."""
        n = self.graph.v()
        order = list()
        bucket = list([] for deg in xrange(n))   # O(V) time
        for node in self.graph.iternodes():   # O(V) time
            bucket[self.graph.degree(node)].append(node)
        maxi = n-1   # last
        for step in xrange(n):   # O(V) time
            while not bucket[maxi]:
                maxi -= 1
            source = bucket[maxi].pop()
            order.append(source)
        for source in order:
            self._greedy_color(source)

    def _greedy_color(self, source):   # a list is faster then a set
        """Give node the smallest possible color."""
        n = self.graph.v()   # memory O(V)
        used = [False] * n   # is color used?
        for target in self.graph.iteradjacent(source):
            if self.color[target] is not None:
                used[self.color[target]] = True
        for c in xrange(n):   # check colors
            if not used[c]:
                self.color[source] = c
                break
        return c

# EOF
