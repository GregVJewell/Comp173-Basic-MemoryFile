from Classes import *

"""
    Memory Dump to show all frames occupied by a program
"""
def dump_Memory():
    print("Total Memory: %d\nFrame Sizes: %d\nNumber of Frames: %s" % (Memory.memory, Memory.size, Memory.frames))
    for x in range(Memory.frames):
        if Memory.table.get(x).free is not True:
            print(Frame.printFrame(Memory.table.get(x)))


"""
    Prompts users to to add a program to memory
    - Automatically increments Program + #
    - Uses First-Fit algorithm
"""
def load():
    pages = int(input("Number of Pages in exe?"))
    index = 0
    page_table = []
    """
    Assuming each page is 1024
    """
    if pages * 1024 > int(Memory.memory):
        print("File requires more memory than currently available, try again!")
        load()
    else:
        program = Program()
        program.pages = pages
        program.size = (1024 * pages)
        program.name = "Program " + str((len(Memory.programs) + 1))
        Memory.programs.update({program.name: program})
        Memory.numProgs += 1

        temp = program.size

        x = 0
        while temp > 0 and x != int(Memory.frames):
            frame = Memory.table.get(x)
            if temp - 512 < 0:
                if frame.free is True:
                    frame.occupied = temp
                    frame.free = False
                    frame.program = program.name

                    Memory.table.update({x: frame})
                    page_table.append([index, x])
                    index += 1

                    temp = temp - frame.occupied
            else:
                if frame.free is True:
                    frame = Memory.table.get(x)
                    frame.free = False
                    frame.program = program.name
                    frame.occupied = 512

                    Memory.table.update({x: frame})
                    page_table.append([index, x])
                    index += 1

                    temp = temp - frame.occupied

            x += 1

        save_Memory()


"""
    Reads into file information to re-build Memory structure
    on fresh starts
"""
def read_Memory():
    print("Reading Memory File!")
    with open('memory.txt', 'r') as file:
        Memory.memory = int(file.readline().strip())
        Memory.size = int(file.readline().strip())
        Memory.frames = int(file.readline().strip())

        buffer = []
        for x in range(Memory.frames):
            buffer.append(file.readline().strip().split(' '))
            Memory.table.update({buffer[x][0]: buffer[x][1]})

            frame = Frame()
            frame.index = x
            frame.size = buffer[x][1]
            frame.free = buffer[x][2]
            frame.program = buffer[x][3]

        file.close()


"""
    Writes the default Memory structure to Memory.txt
"""
def init_Memory():
    print("Initializing Memory File!")
    file = open('memory.txt', 'w')

    file.write('%d\n%d\n%d\n%d\n%s\n' % (Memory.memory, Memory.size, Memory.frames, Memory.numProgs, Memory.programs))

    for x in range(0, Memory.frames):
        frame = Frame()
        frame.index = x
        frame.size = Memory.size
        frame.free = True

        Memory.table.update({x: frame})

        file.write('%d %d %s %s\n' % (frame.index, frame.size, frame.free, frame.program))
    file.close()

    return Memory


"""
    Writes current memory structure to Memory.txt
    for re-use at later time.
"""
def save_Memory():
    print("Saving Memory File!")
    file = open('memory.txt', 'w')
    file.write('%d\n%d\n%d\n%d\n%s\n' % (Memory.memory, Memory.size, Memory.frames, Memory.numProgs, Memory.programs))

    for x in range(0, Memory.frames):
        frame = Memory.table.get(x)
        file.write('%d %d %s %s\n' % (frame.index, frame.size, frame.free, frame.program))

    file.close()


"""
    Frees all frames associated to the given Program Name
"""
def free_Memory(name):
    for x in range(0, Memory.frames):
        if Memory.table.get(x).program == name:
            Memory.table.get(x).free = True
            Memory.table.get(x).program = None

            temp = Memory.programs.get(name)
            del temp
            Memory.numProgs -= 1


"""
    Lists all the frames associated to given Program Name
"""
def list_Program(name):
    for x in range(0, Memory.frames):
        if Memory.table.get(x).program == name:
            Frame.printFrame(Memory.table.get(x))
