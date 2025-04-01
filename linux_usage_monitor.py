#!/usr/bin/env python3

'''
Author : Rajkumar Nagarasa

Description : This python script is a linux system usage monitor tha provide real-time
              information about a system resource usage
'''

import os       # To run system commands
import platform # To get OS info
import shutil   # For disk usage
import time     # For delays

# Get CPU usage using 'top' command (Linux only)
def get_cpu_usage():
    output = os.popen("top -bn1 | grep 'Cpu(s)'").read()
    return output.strip()

# Get memory usage using 'free' command
def get_memory_usage():
    output = os.popen("free -h").read()
    return output.strip()

# Get disk usage using shutil (built-in)
def get_disk_usage():
    total, used, free = shutil.disk_usage("/")
    return {
        "total": total,
        "used": used,
        "free": free
    }

# Get network usage using 'ip -s link' command
def get_network_usage():
    output = os.popen("ip -s link").read()
    return output.strip()

# Print system usage information
def print_usage():
    print("System: " + platform.system() + " " + platform.release())
    
    print("\n  CPU Usage ")
    print(get_cpu_usage())

    print("\n Memory Usage ")
    print(get_memory_usage())

    print("\n Disk Usage ")
    disk = get_disk_usage()
    used_gb = disk["used"] // (1024 ** 3)
    total_gb = disk["total"] // (1024 ** 3)
    print("Used: {} GB / Total: {} GB".format(used_gb, total_gb))

    print("\n Network Usage ")
    print(get_network_usage())

# Run the monitor loop
if __name__ == "__main__":
    while True:
        print("\n=== Linux System Usage Monitor ===")
        print_usage()
        time.sleep(5)

