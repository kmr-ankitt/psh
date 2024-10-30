"""psh: a simple shell written in Python"""

import os
import subprocess


"""
 'cd' command needs to be handled separately as it changes the directory 
of the shell itself and not the child process created by subprocess module. 
"""

def psh_cd(path):
    try:
        os.chdir(os.path.abspath(path))
    except Exception:
        print("cd: no such file or directory: {}".format(path))


def psh_help():
    print("""psh: shell implementation in Python.
          Supports all basic shell commands.""")


def main():
    
    """ Loop runs infinite times until user types 'exit' """
    while True:
        inp = input("> ")
        if inp == "exit":
            break
        elif inp[:3] == "cd ":
            psh_cd(inp[3:])
        elif inp == "help":
            psh_help()
        else:
            execute_command(inp)

