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
