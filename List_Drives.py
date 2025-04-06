#!/usr/bin/env python3

'''
Author: Ian Serquinaa

This file purpose is to list all physical drives and partitions
on a linux system.It execudetes the lsblk command to retrieve the device names
then formats and prints them as device paths. /dev/sda
'''

# Import the subprocess module for this script to run shell commands
import subprocess

# Function to list physical drives using lsblk command
def list_drives():
    # Run the lsblk command to gather lists of device names
    try:
        lsblk_output = subprocess.run( #Execute command in a list
            ["lsblk", "-l", "-o", "NAME"], #Run system with list option & specify that only name should be output
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
    print('\nPhysical Drives:')
    print('-' * 20) # Header divider

    # Skip header line
    for line in lsblk_output[1:]: 
        # If line not empty after stripping whitespace, process
        if line.strip():
            # Adding "/dev/" for device path name
            device = f"/dev/{line.strip()}"
            # Print the device path in a formatted string
            print(f"Device: {device}")

def main():
    list_drives()

if __name__ == "__main__":
    main()

