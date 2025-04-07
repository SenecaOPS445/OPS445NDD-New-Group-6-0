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
Usage: ./Assignment2Testing.py [-a or --all] [-u or --usage] [-l or --list] [-m or --mount] [-r or --report] 

Generate a system report or view individual sections.

options:
  -h, --help    show this help message and exit
  -u, --usage   Show disk usage (df -h).
  -l, --list    List physical drives and partitions.
  -m, --mount  Show mount points from /etc/fstab.
  -a, --all     Generate a full system report without creating a file.
  -r, --report  Generate a full system report and creates a file in the same directory.

```
