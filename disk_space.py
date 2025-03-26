import random

# Do not modify.
class DiskSpace:
    """
    Class representation of computer hard disk storage.
    """
    def __init__(self):
        self.total_capacity_gb = 512

    def available(self):
        in_use = random.uniform(0, self.total_capacity_gb)
        avail = self.total_capacity_gb - in_use 
        return avail
