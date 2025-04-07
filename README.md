# Winter 2025 Assignment 2

## Disk Report Tool for Linux (assignment2.py)
### Authors
- **Andy Persaud Cheteram**
- **Rajkumar Nagarasa**
- **Edison Leung**
- **Ian Serquinaa**

### Description:
This python script is designed to create reports involving verious task about disk.
Such task that can be reported are:
- **Disk Usage**
- **List of Physical drives**
- **Mount point**

This report can be generated in 2 formats:
- **Console Output**
- **Text File Output**

```
Usage: ./assignment2.py [-a or --all] [-u or --usage] [-l or --list] [-m or --mount] [-r or --report] 

Generate a system report or view individual sections.

options:
  -h, --help    show this help message and exit
  -u, --usage   Show disk usage (df -h).
  -l, --list    List physical drives and partitions.
  -m, --mount  Show mount points from /etc/fstab.
  -a, --all     Generate a full system report without creating a file.
  -r, --report  Generate a full system report and creates a file in the same directory.

```

```
Original proposal questions

1. How will your program gather required input?

    Command-Line Arguments: The program will primarily gather input through command-line arguments using the argparse module.
        Arguments will allow users to specify which sections of the disk report to generate (disk usage, drives, mount points, or a full report), and whether to output the report to a file or the terminal.

2. How will your program accomplish its requirements?

    System Commands: The program will use the subprocess module to execute Linux system commands (df -h, lsblk) to gather disk usage and drive information.
    File Reading: The program will read the /etc/fstab file to gather mount point information.
    Data Formatting: The gathered data will be formatted into a readable report, either in plain text for terminal output or file saving.
    Error Handling: The program will include try...except blocks to handle potential errors during command execution and file operations, providing informative error messages within the report.

3. How will output be presented?

    Terminal Output: If no output file is specified, the report will be printed to the terminal.
    Text File Output: If an output file is specified, the report will be saved as a text file in the specified directory. The filename will include a timestamp.

4. What arguments or options will be included?

    -u or --usage: Show disk usage.
    -l or --list: List physical drives and partitions.
    -m or --mount: Show mount points from /etc/fstab.
    -a or --all: Generate a full system report for terminal output.
    -r or --report: Generate a full system report and create a file.

5. What aspects of development do you think will present the most challenge?

    Error Handling: Ensuring robust error handling for all potential scenarios, especially when dealing with external commands and file operations.
    Output formatting: Making the output easy to read.
    Testing: Thoroughly testing the script on different Linux distributions to ensure compatibility.

6. When do you estimate you will complete each part of the task? Provide a rough timeline for planning, coding, testing, and documenting your assignment.

    Planning (1 day):
        Finalize the program's requirements and design.
        Outline the functions and modules to be used.
    Coding (3 days):
        Implement the functions for gathering disk usage, drive information, and mount points.
        Implement the report generation logic.
        Add command-line argument handling using argparse.
    Testing (2 days):
        Test the script with various input arguments.
        Test the script on different Linux distributions.
        Perform error handling tests.
    Documenting (1 day):
        Write the README.md file.
        Add comments to the code.
        Finalize any other documentation.
```
