#!/usr/bin/env python3
'''
Author: Group 6 NDD - Andy Persaud Cheteram, Rajkumar Nagarasa, Edison Leung & Ian Serquinaa

Description: This script generates a system report by integrating the functionality of
             linux_usage_monitor.py, List_Drives.py, and MountChecker.py.
'''

'''
Changes from the original scripts: Removed print statements and returning strings instead, 
allowing generate_report function to control the output and integrate it into the report. 
Simplified error handling from original scripts. Except blocks now return strings instead of prints to be included in report.
'''
import argparse
import subprocess
import datetime

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

    Description: This file purpose is to list all physical drives and partitions
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

    Description: In this script, attached disk (storage) devices are read and checked to see if there mountpoint is boot.
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
                    mount_points.append(f"{parts[0]} is mounted to {parts[1]}.")
        # returns a string with each mount point on a new line, otherwise states no points found
        return "\n".join(mount_points) if mount_points else "No mount points found."
    except (FileNotFoundError, PermissionError) as e:
        return f"Error retrieving mount points: {e}"

def generate_report(output_file=None):
    """Generates the system report."""

    # Gets the current time and date
    now = datetime.datetime.now()
    current_time = f"{now.year}-{now.month:02}-{now.day:02}_{now.hour:02}:{now.minute:02}:{now.second:02}"

    # Implements the current date and time into the file
    if output_file is None:
        output_file = f"Disk_Report_{current_time}.txt"

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

    # Implement argparse to add short cut arguments to request certain tasks.
    parser = argparse.ArgumentParser(
        description="Generate a system report or view individual sections.", 
        usage="./Assignment2Testing.py [-a or --all] [-u or --usage] [-l or --list] [-m or --mounts] [-r or --report] ")
    
    # Check usage using  -u
    parser.add_argument("-u", "--usage", action="store_true", help="Show disk usage (df -h).")
    parser.add_argument("-l", "--list", action="store_true", help="List physical drives and partitions.")
    parser.add_argument("-m", "--mount", action="store_true", help="Show mountpoints from /etc/fstab assioted with boot")
    parser.add_argument("-a", "--all", action="store_true", help="Generate a full system report without creating a file.") 
    parser.add_argument("-r", "--report", action="store_true", help="Generate a full system report and creates a file in the same directory.")

    # Shortens added arguments 
    args = parser.parse_args()

    if args.usage:
    # if argument -u or -usage is used, it will show just disk usage. 
        print("\n--- Disk Usage ---")
        print(show_disk_usage())    

    elif args.list:
    # if argument -l or --list is used, it will list current physical drives and partitions.
        print("\n--- Drives and Partitions ---")
        print(list_drives())
    
    elif args.mounts:
    # if argument -m or --mount is used, it will show currently mounted filesystems that start on boot usage. 
        print("\n--- Mount Points (fstab) ---")
        print(check_fstab())

    elif args.all:
    # if argument -a or --all is used, it will show a full report without creating a file. 
        print("\n----- Full Report -----\n\n")
        print("\n--- Disk Usage ---")
        print(show_disk_usage())
        print("\n--- Drives and Partitions ---")
        print(list_drives())
        print("\n--- Mount Points (fstab) ---")
        print(check_fstab())

    
    elif args.report:
    # if argument -r or --report is used, it will create a report in your current file directory.
        generate_report()

    
    else:
    # If no argument is used, parser will display a usage error message and what the arguments do.
        parser.print_help()
   

