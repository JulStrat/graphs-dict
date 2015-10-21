#!/usr/bin/python

from graphtheory.traversing.dfs import SimpleDFS
from graphtheory.traversing.bfs import SimpleBFS


class FleuryDFS:
    """Fleury's algorithm for finding an Eulerian cycle (multigraphs)."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        if not self._is_eulerian():
            raise ValueError("the graph is not eulerian")
        self.eulerian_cycle = list()   # list of nodes
        self.graph_copy = self.graph.copy()

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = self.graph.iternodes().next()
        node = source
        self.eulerian_cycle.append(node)
        while self.graph_copy.outdegree(node) > 0:
            for edge in list(self.graph_copy.iteroutedges(node)):
                # graph_copy is changing!
                if not self._is_bridge(edge):
                    break
            self.graph_copy.del_edge(edge)
            self.eulerian_cycle.append(edge.target)
            node = edge.target
        del self.graph_copy

    def _is_bridge(self, edge):
        """Bridge test."""
        list1 = list()
        list2 = list()
        algorithm = SimpleDFS(self.graph_copy)
        algorithm.run(edge.source, pre_action=lambda node: list1.append(node))
        self.graph_copy.del_edge(edge)
        algorithm = SimpleDFS(self.graph_copy)
        algorithm.run(edge.source, pre_action=lambda node: list2.append(node))
        # Restore the edge.
        self.graph_copy.add_edge(edge)
        return len(list1) != len(list2)

    def _is_eulerian(self):
        """Test if the graph is eulerian."""
        if self.graph.is_directed():
            # We assume that the graph is strongly connected.
            for node in self.graph.iternodes():
                if self.graph.indegree(node) != self.graph.outdegree(node):
                    return False
        else:
            # We assume that the graph is connected.
            for node in self.graph.iternodes():
                if self.graph.degree(node) % 2 == 1:
                    return False
        return True


class FleuryDFSWithEdges:
    """Fleury's algorithm for finding an Eulerian cycle (multigraphs)."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        if not self._is_eulerian():
            raise ValueError("the graph is not eulerian")
        self.eulerian_cycle = list()   # list of edges

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = self.graph.iternodes().next()
        node = source
        self.graph_copy = self.graph.copy()
        while self.graph_copy.outdegree(node) > 0:
            for edge in list(self.graph_copy.iteroutedges(node)):
                # graph_copy is changing!
                if not self._is_bridge(edge):
                    break
            self.eulerian_cycle.append(edge)
            self.graph_copy.del_edge(edge)
            node = edge.target
        del self.graph_copy

    def _is_bridge(self, edge):
        """Bridge test."""
        list1 = list()
        list2 = list()
        algorithm = SimpleDFS(self.graph_copy)
        algorithm.run(edge.source, pre_action=lambda node: list1.append(node))
        self.graph_copy.del_edge(edge)
        algorithm = SimpleDFS(self.graph_copy)
        algorithm.run(edge.source, pre_action=lambda node: list2.append(node))
        # Restore the edge.
        self.graph_copy.add_edge(edge)
        return len(list1) != len(list2)

    def _is_eulerian(self):
        """Test if the graph is eulerian."""
        if self.graph.is_directed():
            # We assume that the graph is strongly connected.
            for node in self.graph.iternodes():
                if self.graph.indegree(node) != self.graph.outdegree(node):
                    return False
        else:
            # We assume that the graph is connected.
            for node in self.graph.iternodes():
                if self.graph.degree(node) % 2 == 1:
                    return False
        return True


class FleuryBFS:
    """Fleury's algorithm for finding an Eulerian cycle (multigraphs)."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        if not self._is_eulerian():
            raise ValueError("the graph is not eulerian")
        self.eulerian_cycle = list()   # list of nodes
        self.graph_copy = self.graph.copy()

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = self.graph.iternodes().next()
        node = source
        self.eulerian_cycle.append(node)
        while self.graph_copy.outdegree(node) > 0:
            for edge in list(self.graph_copy.iteroutedges(node)):
                # graph_copy is changing!
                if not self._is_bridge(edge):
                    break
            self.graph_copy.del_edge(edge)
            self.eulerian_cycle.append(edge.target)
            node = edge.target
        del self.graph_copy

    def _is_bridge(self, edge):
        """Bridge test."""
        list1 = list()
        list2 = list()
        algorithm = SimpleBFS(self.graph_copy)
        algorithm.run(edge.source, pre_action=lambda node: list1.append(node))
        self.graph_copy.del_edge(edge)
        algorithm = SimpleBFS(self.graph_copy)
        algorithm.run(edge.source, pre_action=lambda node: list2.append(node))
        # Restore the edge.
        self.graph_copy.add_edge(edge)
        return len(list1) != len(list2)

    def _is_eulerian(self):
        """Test if the graph is eulerian."""
        if self.graph.is_directed():
            # We assume that the graph is strongly connected.
            for node in self.graph.iternodes():
                if self.graph.indegree(node) != self.graph.outdegree(node):
                    return False
        else:
            # We assume that the graph is connected.
            for node in self.graph.iternodes():
                if self.graph.degree(node) % 2 == 1:
                    return False
        return True


class FleuryBFSWithEdges:
    """Fleury's algorithm for finding an Eulerian cycle (multigraphs)."""

    def __init__(self, graph):
        """The algorithm initialization."""
        self.graph = graph
        if not self._is_eulerian():
            raise ValueError("the graph is not eulerian")
        self.eulerian_cycle = list()   # list of edges

    def run(self, source=None):
        """Executable pseudocode."""
        if source is None:   # get first random node
            source = self.graph.iternodes().next()
        node = source
        self.graph_copy = self.graph.copy()
        while self.graph_copy.outdegree(node) > 0:
            for edge in list(self.graph_copy.iteroutedges(node)):
                # graph_copy is changing!
                if not self._is_bridge(edge):
                    break
            self.eulerian_cycle.append(edge)
            self.graph_copy.del_edge(edge)
            node = edge.target
        del self.graph_copy

    def _is_bridge(self, edge):
        """Bridge test."""
        list1 = list()
        list2 = list()
        algorithm = SimpleBFS(self.graph_copy)
        algorithm.run(edge.source, pre_action=lambda node: list1.append(node))
        self.graph_copy.del_edge(edge)
        algorithm = SimpleBFS(self.graph_copy)
        algorithm.run(edge.source, pre_action=lambda node: list2.append(node))
        # Restore the edge.
        self.graph_copy.add_edge(edge)
        return len(list1) != len(list2)

    def _is_eulerian(self):
        """Test if the graph is eulerian."""
        if self.graph.is_directed():
            # We assume that the graph is strongly connected.
            for node in self.graph.iternodes():
                if self.graph.indegree(node) != self.graph.outdegree(node):
                    return False
        else:
            # We assume that the graph is connected.
            for node in self.graph.iternodes():
                if self.graph.degree(node) % 2 == 1:
                    return False
        return True

# EOF