def rss_mem_of_pid(pid):
    # Path to the /proc/<pid>/smaps file
    smaps_file = f"/proc/{pid}/smaps"
    
    # Open the smaps file and read its contents
    with open(smaps_file, 'r') as f:
        data = f.read()
    
    # Extract the VmRSS value from the file content (it's on the line starting with 'VmRSS')
    for line in data.splitlines():
        if line.startswith('VmRSS'):
            # Extract the value (in kB) and return it as an integer
            return int(line.split()[1])
    
    # Return 0 if VmRSS is not found
    return 0
