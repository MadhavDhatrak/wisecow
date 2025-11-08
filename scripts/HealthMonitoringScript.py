import psutil
import time 

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_THRESHOLD = 200
LOG_FILE = "health_monitoring.log"


def log_alert(message):
    print(message)
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.ctime()}: {message}\n")

def check_system_health():
 
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"High CPU usage detected: {cpu_usage}%")

    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_THRESHOLD:
        log_alert(f"High Memory usage detected: {memory.percent}%")

  
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        log_alert(f"High Disk usage detected: {disk.percent}%")

    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        log_alert(f"High number of running processes detected: {process_count}")

if __name__ == "__main__":
    check_system_health()