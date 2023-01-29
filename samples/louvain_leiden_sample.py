## HERE I am trying to turn this data structure into a class
## WANT: def class: Comm_det_sample / contains def class: 

class Louvain_Leiden_sample:
    def __init__(self, Louvain_data, Leiden_data):
        self.Louvain_data = Louvain_data
        self.Leiden_data = Leiden_data

    def sample_info(self):
        print("This sample contains 300x its data")

class Louvain_data:
    def __init__(self, modulartities, times, no_of_comms, avg_comm_sizes):
        self.modulartities = modulartities
        self.times = times
        self.no_of_comms = no_of_comms
        self.avg_comm_sizes = avg_comm_sizes

class Leiden_data:
    def __init__(self, modulartities, times, no_of_comms, avg_comm_sizes):
        self.modulartities = modulartities
        self.times = times
        self.no_of_comms = no_of_comms
        self.avg_comm_sizes = avg_comm_sizes