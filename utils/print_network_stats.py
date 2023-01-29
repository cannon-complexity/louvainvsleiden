# Note: Diameter currently broken for disconnected networks

def print_networks_stats(Graph_nx, Network_name = 'Your Network'):

    print(f'Key data summary for {Network_name}')
    print('Number of Nodes =' , nx.number_of_nodes(Graph_nx))
    print('Number of Edges =' , nx.number_of_edges(Graph_nx))
    print('1st moment of degree =' , round(nth_moment(Graph_nx, 1),sigfigs=5))
    print('2nd moment of degree' , round(nth_moment(Graph_nx,2), sigfigs=5))
    print('Avg Clus. Coef.=' , round(nx.average_clustering(Graph_nx), sigfigs=5))
    print('Diameter =' , nx.diameter(Graph_nx))

print_networks_stats(G_Karate_nx)

# # How to make Diameter Work For Networks which are not connected 

# largest_cc = max(nx.connected_components(G_Col_Rel_nx), key=len)

# S = [G_Col_Rel_nx.subgraph(c).copy() for c in nx.connected_components(G_Col_Rel_nx)]
# for subgraph in S:
#     print(nx.diameter(subgraph))