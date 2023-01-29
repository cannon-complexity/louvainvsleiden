import networkx as nx
def nth_moment(Graph_nx, n):
    s = 0
    for node in Graph_nx.nodes:
        s += Graph_nx.degree[node] ** n
    return (s/Graph_nx.number_of_nodes())