## JANKY: Trying to turn this function into one which takes the new class structures

# Function which allows us to take a large sample of Louvain and Leiden partitions and records modularity, ARI, Fowlkes and NMI

def generate_sample(number_of_its, G_igraph):

    Louvain_mod_list, Leiden_mod_list = [], []
    Louvain_time = []
    Leiden_time = []

    G_Louvain_no_of_communities = []
    G_Leiden_no_of_communities = []

    G_Louvain_avg_community_sizes = []
    G_Leiden_avg_community_sizes = []

    for i in range(number_of_its):

        # Note that this time is biased because we are deep copying every partition. 
        # Therefore, we use a separate function to calculate the time for our figures
        # This time measurement should just be considered as a helpful but rough guideline

        Louvain_start = time.time()
        G_Louvain_partitions_list = louvain(G_igraph)
        Louvain_end = time.time()
        Louvain_time.append(copy.deepcopy(Louvain_end - Louvain_start))
        
        Leiden_start = time.time()
        G_Leiden_partitions_list = leiden(G_igraph) 
        Leiden_end = time.time()
        Leiden_time.append(copy.deepcopy(Leiden_end - Leiden_start))

        # Recording Modularity
        
        G_Louvain_mod = calc_modularity_list(G_Louvain_partitions_list)
        Louvain_mod_list.append(copy.deepcopy(G_Louvain_mod))

        G_Leiden_mod = calc_modularity_list(G_Leiden_partitions_list)
        Leiden_mod_list.append(copy.deepcopy(G_Leiden_mod))

        # Recording number of communities 

        G_Louvain_no_of_communities.append(copy.deepcopy(len(G_Louvain_partitions_list[-1])))
        G_Leiden_no_of_communities.append(copy.deepcopy(len(G_Leiden_partitions_list[-1])))
        
        # Recording average size of each community

        G_Louvain_community_sizes = []
        G_Leiden_community_sizes = []
        
        for comm in range(len(G_Louvain_partitions_list[-1])):
            G_Louvain_community_sizes.append(copy.deepcopy(len(G_Louvain_partitions_list[-1][comm])))
        G_Louvain_avg_community_sizes.append(copy.deepcopy(statistics.mean(G_Louvain_community_sizes)))

        for comm in range(len(G_Leiden_partitions_list[-1])):
            G_Leiden_community_sizes.append(copy.deepcopy(len(G_Leiden_partitions_list[-1][comm])))
        G_Leiden_avg_community_sizes.append(copy.deepcopy(statistics.mean(G_Leiden_community_sizes)))

        
    # Putting everything in lists

    r1 = Louvain_data(Louvain_mod_list, Louvain_time, G_Louvain_no_of_communities, G_Leiden_avg_community_sizes)
    r2 = Leiden_data(Leiden_mod_list, Leiden_time, G_Leiden_no_of_communities, G_Leiden_avg_community_sizes)

    print(f'Generated a sample of {number_of_its} iterations of Louvain and Leiden')

    return Louvain_Leiden_sample(r1, r2)
