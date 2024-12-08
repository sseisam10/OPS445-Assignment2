import os

def pids_of_prog(program_name):
    # Use os.popen to call the 'pidof' command and read the output
    pids = os.popen(f'pidof {program_name}').read()
    
    # Return the PIDs as a list of strings
    return pids.split()
