#!/usr/bin/env python3

'''
Author: Ian Serquinaa

This file purpose is to list all physical drives and partitions

'''

# Import the subprocess module for this script to run shell commands
import subprocess

# Function to list physical drives using lsblk command
def list_drives():
    # Run the lsblk command to gather lists of device names
    try:
        lsblk_output = subprocess.run( #Execute command in a list
            ["lsblk", "-l", "-o", "NAME,SIZE,TYPE,MOUNTPOINT"], #Run system with list option & specify that only name should be output
            capture_output=True, # Capture standard output and error
            text=True, # Convert output to sting
            check=True 
        ).stdout.splitlines() # Split the output into a list of lines for easier processing

    # Handles the case where the lsblk command fails
    except subprocess.CalledProcessError:
        print('Error: Could not run lsblk. Ensure it is installed and accessible.')
        return # Exit function if error occurs
    
    # Hadles where lsblk command is not found on the system
    except FileNotFoundError:
        print('Error: lsblk command not found.')
        return # Exit function if lsblk is not available
    

    # Header for the list of physical drives
    print('\nPhysical Drives and Partitions')
    print('-' * 30) # Header divider

    # Iterate each line in lslk output and print it, showing raw device info
    for line in lsblk_output:
        print(line)

def main():
    list_drives()

if __name__ == "__main__":
    main()

