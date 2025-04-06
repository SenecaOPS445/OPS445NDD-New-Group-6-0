#!/usr/bin/env python3

'''
Author : Rajkumar Nagarasa

Description : This python script retrieves and displays disk usage information 
              for all mounted filesystems on a Linux machine.
'''

import subprocess  

# Function to show disk usage
# Run the 'df -h' command to get disk usage 
def show_disk_usage():
    try:
        
        output = subprocess.run(
            ["df", "-h"],              
            capture_output=True,       
            text=True,                 
            check=True                 
        ).stdout  # Get the standard output from the command

        print("\nDisk Usage:")

        # Print the full 'df -h' output
        print(output)

    except subprocess.CalledProcessError:
        # If 'df' fails to run or exits with an error code
        print("Error: Could not retrieve disk usage using df.")
    except FileNotFoundError:
        # If the 'df' command is not available (very rare on Linux)
        print("Error: 'df' command not found on this system.")

# Main function to run the program
def main():
    show_disk_usage()


if __name__ == "__main__":
    main()
