import psutil

# Define thresholds
CPU_THRESHOLD = 80  # CPU usage threshold in percent
MEMORY_THRESHOLD = 80  # Memory usage threshold in percent
DISK_THRESHOLD = 80  # Disk usage threshold in percent

# Function to check CPU usage
def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > CPU_THRESHOLD:
        print(f"CPU usage is high: {cpu_percent}%")

# Function to check memory usage
def check_memory_usage():
    memory_percent = psutil.virtual_memory().percent
    if memory_percent > MEMORY_THRESHOLD:
        print(f"Memory usage is high: {memory_percent}%")

# Function to check disk usage
def check_disk_usage():
    disk_percent = psutil.disk_usage('/').percent
    if disk_percent > DISK_THRESHOLD:
        print(f"Disk usage is high: {disk_percent}%")

# Function to check running processes
def check_running_processes():
    num_processes = len(psutil.pids())
    print(f"Number of running processes: {num_processes}")

# Main function to monitor system health
def monitor_system_health():
    print("Monitoring system health...")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if __name__ == "__main__":
    monitor_system_health()
