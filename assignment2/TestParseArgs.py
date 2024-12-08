
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
