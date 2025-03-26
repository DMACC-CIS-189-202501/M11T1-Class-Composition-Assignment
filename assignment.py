# TODO 1: Add a file level Docstring


from memory import Memory
from disk_space import DiskSpace


class Computer:
    """
    Computer class. 
    
    Attributes:
        name: str
            Passed in as an argument to the constructor.
        

    Methods: 
        get_info:
            Returns a string of the form:

            [timestamp] computer name: <name>, available memory: <available memory>, available storage: <available storage>
    
    """


    # TODO 2: Finish creating the init function to store the name (a string), memory (a memory object), and disk_space (a disk_space object)
    def __init__(self, name, memory, disk_space):
        pass
    
    # TODO 3: Finish the get_info Method
    def get_info(self):
        # Get current timestamp; finish this code
        time_stamp = None

        # Get Name from Computer Object; finish this code
        name = None

        # Get Memory availible from Memory Object; call Memory.available() from the object stored within your computer
        # finish this code
        memory = None

        # Get Disk Space availible from Disk Object; call DiskSpace.available() from the object stored within your computer
        # finish this code
        disk_space = None

        #Construct and return the string
        return f"[{time_stamp}]: computer name: {name}, available memory: {memory}, available storage: {disk_space}"



# TODO 4: Finish the main method
def main():


    machine_names = ["RQS445", "MIKES-MACHINE", "Leet-315"]

    # For each of the machine_names, create an instance of the Computer
    # class, then call `get_info` for each. 

    for name in machine_names:
        # Create a memory Object; finish this line
        mem_obj = None
        # Create disk space object; finish this line
        disk_space_obj = None
        # Create a Compuer object, passing in the namme, memory, and disk_space; finish this line
        computer = Computer()

        #Print out the string
        print(computer.get_info())

if __name__ == "__main__":
    main()