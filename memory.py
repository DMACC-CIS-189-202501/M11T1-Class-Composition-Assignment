import random


# Do not modify.
class Memory:
    """
    Class representation of computer memory.
    """
    def __init__(self):

        self.total_ram_gb = 16

    def available(self):
        in_use = random.uniform(0, self.total_ram_gb)
        avail = self.total_ram_gb - in_use 
        return avail