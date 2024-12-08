def get_sys_mem():
    """
    Reads and returns the total system memory from /proc/meminfo.
    :return: Total memory in kilobytes (int).
    """
    try:
        with open('/proc/meminfo', 'r') as meminfo:
            for line in meminfo:
                if line.startswith('MemTotal:'):
                    # Extract and return the value in kilobytes
                    return int(line.split()[1])
    except Exception as e:
        print(f"Error reading /proc/meminfo: {e}")
        return None


def get_avail_mem():
    """
    Reads and returns the available memory from /proc/meminfo.
    :return: Available memory in kilobytes (int).
    """
    try:
        with open('/proc/meminfo', 'r') as meminfo:
            for line in meminfo:
                if line.startswith('MemAvailable:'):
                    # Extract and return the value in kilobytes
                    return int(line.split()[1])
    except Exception as e:
        print(f"Error reading /proc/meminfo: {e}")
        return None
