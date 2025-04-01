#!/usr/bin/env python3
'''
Author: Andy Persaud Cheteram

This file is created to check boot drives to see if 
they are mounted at boot using the file /etc/fstab 
'''


# Documentation W.I.P 

import sys

def check_fstab():
    '''
    Reads the /etc/fstab file and prints the mount points and devices that are mounted at boot.
    Handles FileNotFoundError and PermissionError exceptions.
    '''
    try: 
        f = open('/etc/fstab', 'r') # Open the /etc/fstab file for reading.
        lines = f.readlines() # Read all the lines from the file into a list.
        f.close() # Close the file when we're done.

        for line in lines: # Go through each line in the file.
            """"Remove any extra spaces or tabs at the beginning or end of the line.""""
            line = line.strip()

            # Check if the line is not empty and isn't a comment (lines starting with #).
            if line and not line.startswith("#"):
                # Split the line into individual parts, separated by spaces.
                parts = line.split()
                # Make sure the line has at least two parts (the drive and its mount point).
                if len(parts) >= 2:
                    # Print out the drive and where it's mounted.
                    print(f"{parts[0]} mounted -> {parts[1]} at boot")

    # If the /etc/fstab file is missing, tell the user.
    except FileNotFoundError:
        print("Error: /etc/fstab not found.")
    # If we don't have permission to read the file, tell the user.
    except PermissionError:
        print("Error: Permission deined when reading /etc/stab.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-m": # -m is a placeholder for argpause
        check_fstab()
    else:
        print("Usage: ./MountChecker.py -m")
                          

                
