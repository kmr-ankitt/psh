import os
import subprocess
def psh_cd(path):
    try:
        os.chdir(os.path.abspath(path))
    except Exception:
        print("cd: no such file or directory: {}".format(path))
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
