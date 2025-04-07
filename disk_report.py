#!/usr/bin/env python3
'''
Author: Edison Leung

Description: This script generates a system report by integrating the functionality of
             linux_usage_monitor.py, List_Drives.py, and MountChecker.py.
'''

'''
Changes from the original scripts: Removed print statements and returning strings instead, allowing generate_report function to control the output and integrate it into the report. Simplified error handling from original scripts. Except blocks now return strings instead of prints to be included in report.
'''

import argparse
import subprocess

# Function to show disk usage
# Run the 'df -h' command to get disk usage 
def show_disk_usage():
    '''
    Author : Rajkumar Nagarasa

    Description : This python script retrieves and displays disk usage information 
                  for all mounted filesystems on a Linux machine.
    '''
    try:
        output = subprocess.run(
            ["df", "-h"],
            capture_output=True,
            text=True,
            check=True
        ).stdout    # Get the standard output from the command
        return output
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        return f"Error retrieving disk usage: {e}"

# Function to list physical drives using lsblk command
def list_drives():
    '''
    Author: Ian Serquinaa

    This file purpose is to list all physical drives and partitions
    on a linux system.It execudetes the lsblk command to retrieve the device names
    then formats and prints them as device paths. /dev/sda
    '''
    # Run the lsblk command to gather lists of device names
    try:
        output = subprocess.run(    #Execute command in a list
            ["lsblk", "-l", "-o", "NAME,SIZE,TYPE,MOUNTPOINT"], #Run system with list option & specify that only name should be output
            capture_output=True,    # Capture standard output and error
            text=True,  # Convert output to sting
            check=True
        ).stdout
        return output
    # Handles the case where the lsblk command fails
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        return f"Error retrieving drives info: {e}"


'''
Reads the /etc/fstab file and prints the mount points and devices that are mounted at boot.
Handles FileNotFoundError and PermissionError exceptions.
'''
def check_fstab():
    '''
    Author: Andy Persaud Cheteram

    This file is created to check boot drives to see if 
    they are mounted at boot using the file /etc/fstab 
    '''
    try:
        '''Changed from original to ensure that ensures that the file is automatically closed when
        the with block finishes, even if exceptions occur'''
        with open('/etc/fstab', 'r') as f: # Open the /etc/fstab file for reading.
            lines = f.readlines()   # Read all the lines from the file into a list.
        '''Storing mount points in a list'''
        mount_points = []   
        for line in lines:  # Go through each line in the file.
            '''Remove any extra spaces or tabs at the beginning or end of the line.'''
            line = line.strip()

            # Check if the line is not empty and isn't a comment (lines starting with #).
            if line and not line.startswith("#"):
                # Split the line into individual parts, separated by spaces.
                parts = line.split()
                # Make sure the line has at least two parts (the drive and its mount point).
   
                if len(parts) >= 2:
                    mount_points.append(f"{parts[0]} mounted -> {parts[1]} at boot")
        # returns a string with each mount point on a new line, otherwise states no points found
        return "\n".join(mount_points) if mount_points else "No mount points found."
    except (FileNotFoundError, PermissionError) as e:
        return f"Error retrieving mount points: {e}"

def generate_report(output_file=None):
    """Generates the system report."""

    # Initializes report with header
    report = "    Disk Report    \n\n"

    # Add Disk Usage section to the report.
    report += "--- Disk Usage ---\n"
    report += f"{show_disk_usage()}\n\n"

    # Add Drives and Partitions section to the report.
    report += "--- Drives and Partitions ---\n"
    report += f"{list_drives()}\n\n"

    # Add Mount Points (fstab) section to the report.
    report += "--- Mount Points (fstab) ---\n"
    report += f"{check_fstab()}\n"
    
    # Check if an output file was specified.
    if output_file:
        try:
            with open(output_file, 'w') as f:
                f.write(report)
            print(f"Report saved to {output_file}") # Inform the user that the report was saved.
        except Exception as e:
            # Handle any exceptions that occur during file writing.
            print(f"Error saving report: {e}")
    else:
        # If no output file was specified, print the report to the console.
        print(report)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a system report.")
    # output file
    parser.add_argument("-o", "--output", help="Output file for the report.")
    args = parser.parse_args()

    generate_report(args.output)


