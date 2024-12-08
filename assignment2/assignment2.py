#!/usr/bin/env python3

'''
OPS445 Assignment 2
Program: assignment2.py 
Author: "Suyib Shahir Eisam"
Semester: "Fall 2024"

The python code in this file is original work written by
"Suyib Shahir Eisam". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.



'''

import argparse
import os, sys

def parse_command_args() -> object:
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts",epilog="Copyright 2023")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    # add argument for "human-readable". USE -H, don't use -h! -h is reserved for --help which is created automatically.
    # check the docs for an argparse option to store this as a boolean.
    parser.add_argument("program", type=str, nargs='?', help="if a program is specified, show memory use of all associated processes. Show only total use is not.")
    args = parser.parse_args()
    return args
# create argparse function
# -H human readable
# -r running only

def percent_to_graph(percent: float, length: int=20) -> str:
    "turns a percent 0.0 - 1.0 into a bar graph"
    ...
# percent to graph function

def get_sys_mem() -> int:
    "return total system memory (used or available) in kB"
    ...

def get_avail_mem() -> int:
    "return total memory that is available"
    ...

def pids_of_prog(app_name: str) -> list:
    "given an app name, return all pids associated with app"
    ...

def rss_mem_of_pid(proc_id: str) -> int:
    "given a process id, return the resident memory used, zero if not found"
    ...

def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    "turn 1,024 into 1 MiB, for example"
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']  # iB indicates 1024
    suf_count = 0
    result = kibibytes 
    while result > 1024 and suf_count < len(suffixes):
        result /= 1024
        suf_count += 1
    str_result = f'{result:.{decimal_places}f} '
    str_result += suffixes[suf_count]
    return str_result

if __name__ == "__main__":
    args = parse_command_args()
    if not args.program:
        ...
    else:
        ...
    # process args
    # if no parameter passed, 
    # open meminfo.
    # get used memory
    # get total memory
    # call percent to graph
    # print

    # if a parameter passed:
    # get pids from pidof
    # lookup each process id in /proc
    # read memory used
    # add to total used
    # percent to graph
    # take total our of total system memory? or total used memory? total used memory.
    # percent to graph.

#Test Percent
def percent_to_graph(pcnt, max_length):
    """
    Converts a percentage value (0.0 to 1.0) into a graph with symbols (#) and spaces.
    """
    num_symbols = round(pcnt * max_length)
    num_spaces = max_length - num_symbols
    return '#' * num_symbols + ' ' * num_spaces

#TestMemFuncs

def get_sys_mem():
    """
    Reads and returns the total system memory from /proc/meminfo.
    """
    try:
        with open('/proc/meminfo', 'r') as meminfo:
            for line in meminfo:
                if line.startswith('MemTotal:'):
                    # Extract the value in kB
                    return int(line.split()[1])
    except Exception as e:
        print(f"Error reading /proc/meminfo: {e}")
        return None


def get_avail_mem():
    """
    Reads and returns the available memory from /proc/meminfo.
    """
    try:
        with open('/proc/meminfo', 'r') as meminfo:
            for line in meminfo:
                if line.startswith('MemAvailable:'):
                    # Extract the value in kB
                    return int(line.split()[1])
    except Exception as e:
        print(f"Error reading /proc/meminfo: {e}")
        return None

#TestParseArgs

#TestPidList
import os

def pids_of_prog(program_name):
    # Use os.popen to call the 'pidof' command and read the output
    pids = os.popen(f'pidof {program_name}').read()
    
    # Return the PIDs as a list of strings
    return pids.split()

#TestPidMem
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

#TestParseArgs
import unittest
import sys
import os
import subprocess as sp
from importlib import import_module

class TestParseArgs(unittest.TestCase):
    "Test if parse_command_args is working"

    def setUp(self):
        # Define the filename and Python executable path
        self.filename = 'assignment2.py'
        self.pypath = sys.executable
        error_output = f'{self.filename} cannot be found (HINT: make sure this script AND your file are in the same directory)'
        
        # Check if the file exists in the current directory
        file = os.path.join(os.getcwd(), self.filename)
        self.assertTrue(os.path.exists(file), msg=error_output)
        
        # Try to import the module for testing
        try:
            self.a2 = import_module(self.filename.split('.')[0])
        except ModuleNotFoundError:
            print("Cannot find a function inside your assignment2.py. Do not rename or delete any of the required functions.")

    def test_argparse_help(self):
        "Test if `assignment2.py -h` returns the required options"
        
        # Run the script with the -h flag using subprocess
        p = sp.Popen(['/usr/bin/python3', self.filename, '-h'], stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE)
        stdout, err = p.communicate()
        
        # Wait for the process to finish
        return_code = p.wait()
        
        # Error message if the command fails
        error_output = 'Output of `assignment2.py -h` doesn\'t match what\'s expected. Make sure you\'ve added an option!)'
        
        # Expected output in the help message
        expected_out = ["[-h]", "[-H]", "[-l LENGTH]", "[program]"]
        
        # Check if each expected output string is present in the stdout
        for string in expected_out:
            self.assertIn(string, stdout.decode('utf-8'), msg=error_output)
