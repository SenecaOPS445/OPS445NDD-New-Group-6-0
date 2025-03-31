import subprocess

def list_drives():
#list all drives and partitions device names using lsblk
    try:
        lsblk_output = subprocess.run(
            ["lsblk", "-l", "-o", "NAME"],
            capture_output=True, 
            text=True, 
            check=True
        ).stdout.splitlines()
    except subprocess.CalledProcessError:
        print('Error: Could not run lsblk. Ensure it is installed and accessible.')
        return
    except FileNotFoundError:
        print('Error: lsblk command not found.')
        return
    

    # Print header
    print('\nPhysical Drives:')
    print('-' * 20)

    # Skip header line
    for line in lsblk_output[1:]: 
        if line.strip():
            device = f"/dev/{line.strip()}"
            print(f"Device: {device}")

def main():
    list_drives()

if __name__ == "__main__":
    main()

