from comm_det.louvain import louvain_test , louvain
louvain_test()

import networkx as nx



from utils.nth_moment import nth_moment

G_Karate_nx = nx.read_gexf('/Users/lewishome/Ground_truth_sample_graphs/gexf_format/karate_club_graph.gexf')
print('TYPE OF OBJECT IS' ,type(G_Karate_nx))







print(nth_moment(G_Karate_nx, 2))


# import igraph as ig
# G_Karate = ig.Graph.Read_GraphML('/Users/lewishome/Ground_truth_sample_graphs/graph_ml_format/karate_club_graph.graphml')
#louvain(G_Karate)