from os import listdir, remove
from MemoryFunctions import *


def main():  # Mainly just the simple menu
    init_Memory()
    while True:
        print("What would you like to do?")
        print("[0] Load Program")
        print("[1] Initialize")
        print("[2] Dump")
        print("[3] Reset")
        print("[4] Free Program")
        print("[5] List Program")
        print("[6] Exit")
        answer = input()

        if answer == '0':
            load()
        elif answer == '1':
            init_Memory()
        elif answer == '2':
            dump_Memory()
        elif answer == '3' and 'memory.txt' in listdir():
            remove('memory.txt')
            Memory.numProgs = 0
            Memory.programs = {}
            init_Memory()
        elif answer == '4':
            name = input("Enter program to free: ")
            free_Memory(name)
        elif answer == '5':
            name = input("Enter program to list: ")
            list_Program(name)
        elif answer == '6':
            save_Memory()
            exit(0)

        else:
            print("Incorrect Input, please attempt again")
            main()


main()
