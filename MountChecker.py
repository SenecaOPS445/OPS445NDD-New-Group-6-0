#!/usr/bin/env python3
'''
Author: Andy Persaud Cheteram

This file is created to check boot drives to see if 
they are mounted at boot using the file /etc/fstab 
'''

import sys

def check_fstab():
    try: 
        f = open('/etc/fstab', 'r')
        lines = f.readlines()
        f.close()

        for line in lines:
            line = line.strip()

            if line and not line.startswith("#"):
                parts = line.split()      
                if len(parts) >= 2:       
                    print(f"{parts[0]} mounted -> {parts[1]} at boot")

    except FileNotFoundError:
        print("Error: /etc/fstab not found.")
    except PermissionError:
        print("Error: Permission deined when reading /etc/stab.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-m": # -m is a placeholder for argpause
        check_fstab()
    else:
        print("Usage: ./MountChecker.py -m")
                          

                