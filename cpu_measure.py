import psutil
import time

def monitor_cpu(interval=1):
    print(f"Monitoring CPU usage... (Press CTRL+C to stop)")
    print("-" * 40)
    
    try:
        while True:
            # Get the total CPU usage percentage
            # interval=1 means it blocks for 1 second to calculate the average usage over that second
            total_usage = psutil.cpu_percent(interval=interval)
            
            # Get usage for each individual core
            per_core_usage = psutil.cpu_percent(interval=None, percpu=True)
            
            # Formatting the per-core data for cleaner output
            per_core_str = " | ".join([f"{core}%" for core in per_core_usage])
            
            print(f"Total Usage: {total_usage}%")
            print(f"Per Core:    [{per_core_str}]")
            print("-" * 80)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    monitor_cpu()ð