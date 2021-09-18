from help import ProgramUsage

def application_start(argv, env):
    if len(argv) < 2:
        print(ProgramUsage)
    return 0
