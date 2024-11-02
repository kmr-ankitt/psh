"""psh: a simple shell written in Python"""

import os
import subprocess


"""Function handles all commands except 'cd' and 'exit' commands of psh shell"""
def execute_command(command):
    try:
        if "|" in command:
            
            """Storing the original values of stdin and stdout"""
            s_in, s_out = (0, 0)
            s_in = os.dup(0)
            s_out = os.dup(1)

            fdin = os.dup(s_in)

            """Iterating over all piped commands"""
            for cmd in command.split("|"):

                """If first command, fdin is stdin, else it is the readable end of the pipe"""
                os.dup2(fdin, 0)
                os.close(fdin)

                """If it is the last command then restore stdout to original value, 
                else create a piping between fdin and fdout to take input from previous
                command and give output to next command""" 
                
                if cmd == command.split("|")[-1]:
                    fdout = os.dup(s_out)
                else:
                    fdin, fdout = os.pipe()

                # redirect stdout to pipe
                os.dup2(fdout, 1)
                os.close(fdout)

                try:
                    subprocess.run(cmd.strip().split())
                except Exception:
                    print("psh: command not found: {}".format(cmd.strip()))

            """Restoring the original values of stdin and stdout"""
            os.dup2(s_in, 0)
            os.dup2(s_out, 1)
            os.close(s_in)
            os.close(s_out)
        else:
            """If no piping is required, simply run the command"""
            subprocess.run(command.split(" "))

    except Exception:
        print("psh: command not found: {}".format(command))


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

if '__main__' == __name__:
    main()
