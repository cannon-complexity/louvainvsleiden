## Function which runs each algorithm n times on a network

def generate_sample_time(G_igraph, number_of_its, network_name):

    Louvain_time = []
    Leiden_time = []

    for i in range(number_of_its):
        
        Louvain_start = time.time_ns()
        louvain_pure(G_igraph)
        Louvain_end =time.time_ns()

        Louvain_time.append(copy.deepcopy((Louvain_end - Louvain_start ) / (10 ** 9) ))
        
        Leiden_start = time.time_ns()
        leiden_pure(G_igraph) 
        Leiden_end = time.time_ns()
        Leiden_time.append(copy.deepcopy((Leiden_end - Leiden_start)/ (10 ** 9) ))

    
    Louvain_time_mean = statistics.mean(Louvain_time)
    Louvain_time_std = statistics.stdev(Louvain_time)
    Leiden_time_mean = statistics.mean(Leiden_time)
    Leiden_time_std = statistics.stdev(Leiden_time)

    times_data = quick_df(network_name, Louvain_time_mean, Louvain_time_std, Leiden_time_mean, Leiden_time_std)

    print(times_data)
    
    return times_data