class Settings(object):
    def __init__(self):
        self.slurm_partition = 'day'
        self.slurm_num_gpus  = 1
        self.slurm_num_cpus  = 4
        self.slurm_time      = None
        self.slurm_num_nodes = 1
