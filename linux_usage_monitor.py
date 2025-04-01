#!/usr/bin/env python3

'''
Author : Rajkumar Nagarasa

Description : This python script is a linux system usage monitor tha provide real-time
              information about a system resource usage
'''


import psutil           # For system and process utilities (CPU, memory)
import platform         # To get OS information
import shutil           # To get disk usage info
import time             # To create delay in the loop

# Function to get CPU usage percentage
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)  # Measure CPU usage over a 1-second interval

# Function to get memory usage details
def get_memory_usage():
    mem = psutil.virtual_memory()  # Get virtual memory info
    return {
        "total": mem.total,        # Total RAM
        "used": mem.used,          # Used RAM
        "percentage": mem.percent  # Memory usage percentage
    }

# Function to get disk usage details
def get_disk_usage():
    disk = shutil.disk_usage("/")  # Get disk usage for root directory
    return {
        "total": disk.total,       # Total disk size
        "used": disk.used,         # Disk space used
        "free": disk.free,         # Free disk space
        "percentage": (disk.used / disk.total) * 100  # Calculate used percentage manually
    }

# Function to get network usage (total bytes sent and received)
def get_network_usage():
    net_io = psutil.net_io_counters()  # Get network I/O statistics
    return {
        "bytes_sent": net_io.bytes_sent,   # Total bytes sent since boot
        "bytes_recv": net_io.bytes_recv    # Total bytes received since boot
    }

# Function to print system usage in a readable format
def print_usage():
    # Print OS info
    print(f"System: {platform.system()} {platform.release()}")  
    
    # Print CPU usage
    print(f"CPU Usage: {get_cpu_usage()}%")

    # Get and print memory usage
    mem = get_memory_usage()
    print(f"Memory Usage: {mem['used'] / (1024 ** 3):.2f} GB / {mem['total'] / (1024 ** 3):.2f} GB ({mem['percentage']}%)")

    # Get and print disk usage
    disk = get_disk_usage()
    print(f"Disk Usage: {disk['used'] / (1024 ** 3):.2f} GB / {disk['total'] / (1024 ** 3):.2f} GB ({disk['percentage']:.2f}%)")

    # Get and print network usage
    net = get_network_usage()
    print(f"Network - Sent: {net['bytes_sent'] / (1024 ** 2):.2f} MB | Received: {net['bytes_recv'] / (1024 ** 2):.2f} MB")

# Entry point of the script
if __name__ == "__main__":
    # Run the usage monitor in a loop every 5 seconds
    while True:
        print("\n=== Linux System Usage ===")  
        print_usage()                         
        time.sleep(5)                         # Wait for 5 seconds before repeating
