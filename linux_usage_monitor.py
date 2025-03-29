import os
import time
import platform

def get_cpu_usage():
    with open("/proc/stat", "r") as f:
        first_line = f.readline()
    cpu_times = list(map(int, first_line.strip().split()[1:]))
    idle_time = cpu_times[3]
    total_time = sum(cpu_times)

    time.sleep(1)

    with open("/proc/stat", "r") as f:
        second_line = f.readline()
    cpu_times_2 = list(map(int, second_line.strip().split()[1:]))
    idle_time_2 = cpu_times_2[3]
    total_time_2 = sum(cpu_times_2)

    idle_delta = idle_time_2 - idle_time
    total_delta = total_time_2 - total_time

    cpu_usage = 100 * (1.0 - (idle_delta / total_delta))
    return round(cpu_usage, 2)

def get_memory_usage():
    meminfo = {}
    with open("/proc/meminfo", "r") as f:
        for line in f:
            parts = line.split(":")
            key = parts[0]
            value = int(parts[1].strip().split()[0])
            meminfo[key] = value

    total = meminfo["MemTotal"]
    free = meminfo["MemFree"] + meminfo["Buffers"] + meminfo["Cached"]
    used = total - free
    percentage = (used / total) * 100

    return total, used, round(percentage, 2)

def get_disk_usage():
    stat = os.statvfs('/')
    total = (stat.f_blocks * stat.f_frsize) / (1024 ** 3)
    free = (stat.f_bfree * stat.f_frsize) / (1024 ** 3)
    used = total - free
    percentage = (used / total) * 100
    return round(total, 2), round(used, 2), round(percentage, 2)

def get_network_usage():
    with open("/proc/net/dev", "r") as f:
        lines = f.readlines()[2:]

    total_recv = 0
    total_sent = 0

    for line in lines:
        parts = line.strip().split()
        recv = int(parts[1])
        sent = int(parts[9])
        total_recv += recv
        total_sent += sent

    return round(total_sent / (1024 ** 2), 2), round(total_recv / (1024 ** 2), 2)

def print_usage():
    print("\n=== Linux System Usage Monitor ===")
    print("System: {} {}".format(platform.system(), platform.release()))
    print("CPU Usage: {}%".format(get_cpu_usage()))

    total_mem, used_mem, mem_percent = get_memory_usage()
    print("Memory Usage: {:.2f} MB / {:.2f} MB ({:.2f}%)".format(used_mem / 1024, total_mem / 1024, mem_percent))

    total_disk, used_disk, disk_percent = get_disk_usage()
    print("Disk Usage: {:.2f} GB / {:.2f} GB ({:.2f}%)".format(used_disk, total_disk, disk_percent))

    sent, recv = get_network_usage()
    print("Network - Sent: {:.2f} MB | Received: {:.2f} MB".format(sent, recv))

if __name__ == "__main__":
    while True:
        print_usage()
        time.sleep(5)