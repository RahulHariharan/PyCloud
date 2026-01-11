import psutil

def count_partitions():
    # Fetch all disk partitions
    # all=False ignores virtual/internal file systems like /proc
    partitions = psutil.disk_partitions(all=False)
    
    print("--- Detected Partitions ---")
    for p in partitions:
        print(f"Device: {p.device} | Mountpoint: {p.mountpoint} | Type: {p.fstype}")
    
    print("---------------------------")
    print(f"Total physical partitions detected: {len(partitions)}")

if __name__ == "__main__":
    count_partitions()