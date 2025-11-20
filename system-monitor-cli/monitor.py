import psutil
import argparse
import time
import os
import sys # Used for clean script exiting

def get_system_snapshot():
    """Fetches and prints the current CPU, memory, and disk usage."""

    # 1. CPU Usage: interval=0.1 waits briefly for an accurate reading
    cpu_percent = psutil.cpu_percent(interval=0.1)

    # 2. Memory Usage: Calculate total, used, and percentage
    memory = psutil.virtual_memory()
    mem_percent = memory.percent
    mem_used_gb = memory.used / (1024 ** 3)  # Convert bytes to GB
    mem_total_gb = memory.total / (1024 ** 3)

    # 3. Disk Usage (for the current root partition)
    try:
        disk = psutil.disk_usage('/')
        disk_percent = disk.percent
    except:
        disk_percent = "N/A" 

    # --- Print Snapshot ---
    print("\n--- SYSTEM SNAPSHOT ---")
    print(f"**CPU Usage:** {cpu_percent}%")
    print(f"**Memory:** {mem_percent}% used ({mem_used_gb:.2f} GB / {mem_total_gb:.2f} GB)")
    print(f"**Disk Usage:** {disk_percent}%") 
    print("-----------------------\n")


def display_processes(sort_key='cpu', limit=10):
    """
    Fetches running processes, sorts them by the given key, and displays the top N.
    """
    process_data = []

    # Iterate over all running processes
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            pinfo = proc.info

            # Filter out idle processes
            if pinfo['cpu_percent'] == 0.0 and pinfo['memory_percent'] == 0.0:
                continue

            process_data.append({
                'pid': pinfo['pid'],
                'name': pinfo['name'],
                'cpu_percent': pinfo['cpu_percent'],
                'memory_percent': pinfo['memory_percent']
            })

        # Gracefully handle processes that disappear or deny access
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    # --- Sorting Logic ---
    if sort_key == 'memory':
        sorted_processes = sorted(
            process_data,
            key=lambda p: p['memory_percent'],
            reverse=True  
        )
    else: # Default is 'cpu'
        sorted_processes = sorted(
            process_data,
            key=lambda p: p['cpu_percent'],
            reverse=True  
        )

    # --- Display Logic ---
    print(f"\n--- TOP {limit} PROCESSES (Sorted by {sort_key.upper()}) ---")

    # Column Headers: Fixed width formatting
    print(f"{'PID':<6} {'CPU%':<6} {'MEM%':<6} {'PROCESS NAME':<40}")
    print("-" * 60)

    # Print the top processes
    for proc in sorted_processes[:limit]:
        print(
            f"{proc['pid']:<6}"
            f"{proc['cpu_percent']:<6.1f}" 
            f"{proc['memory_percent']:<6.1f}"
            f"{proc['name']:<40.40}"
        )
    print("-" * 60)

    return sorted_processes


def main():
    # 1. Setup Argument Parsing
    parser = argparse.ArgumentParser(
        description="A simple CLI tool to monitor system resources and processes in real-time."
    )
    
    # Sorting argument
    parser.add_argument(
        '-s', '--sort',
        type=str,
        default='cpu',
        choices=['cpu', 'memory'],
        help='Field to sort the process list by (default: cpu).'
    )
    
    # Interval argument
    parser.add_argument(
        '-i', '--interval',
        type=float,
        default=1.0,
        help='Refresh interval in seconds (default: 1.0).'
    )
    
    args = parser.parse_args()
    
    # 2. Start the Real-Time Loop
    while True:
        try:
            # Clear the terminal screen using os.system
            os.system('cls' if os.name == 'nt' else 'clear') 
            
            # Call the display functions using the parsed arguments
            get_system_snapshot() 
            display_processes(sort_key=args.sort, limit=10)

            # Pause for the specified interval
            time.sleep(args.interval)

        except KeyboardInterrupt:
            # Handle Ctrl+C press gracefully
            print("\nMonitor stopped by user.")
            sys.exit(0)
        except Exception as e:
            # Catch unexpected errors and stop the monitor
            print(f"\nAn unexpected error occurred: {e}. Stopping monitor.")
            sys.exit(1)

if __name__ == "__main__":
    main()