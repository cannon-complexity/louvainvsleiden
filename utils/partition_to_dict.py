# Function which converts Louvain and Leiden output partition format into networkx partition dictionary format

def partition_to_dict(partition_list, nxGraph, clustering_label):
    d = {}
    complex_list = nx.get_node_attributes(nxGraph, clustering_label)
    keys = list(complex_list.values())
    
    for i in complex_list.values():
        d[i] = -1
    
    for i in range(len(partition_list)):
        for j in range(len(partition_list[i])):
            #assert(keys[partition_list[i][j]] in d)
            d[keys[partition_list[i][j]]] = i
    return d