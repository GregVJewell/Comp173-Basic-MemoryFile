class Memory:
    memory = 524288     # Total Bytes in 512KB
    size = 512          # Size per Frame (Bytes)
    frames = 1024       # Total Frames Specified in Docs
    table = {}          # Frame Table
    programs = {}       # Exe List
    numProgs = 0     # Number of Exes in Memory


class Frame:
    index = None    # Frame Number
    occupied = 0    # Amount of Used Frame
    total = None    # Size in Bytes
    free = True     # Free or Occupied
    program = None  # Program Holding Frame

    def printFrame(self):
        print("Frame #:", self.index)
        print(self.size, "bytes")

        if self.free:
            print("Status: Free")
        elif self.free is False:
            print("Status: Occupied")

        print("Program Holding Frame: ", self.program)


class Program:
    name = None     # Key for Exe
    size = None     # Size of Exe
    pages = None    # User input size of Exe
    table = {}      # Page Table for Exe
