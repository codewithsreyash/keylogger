import psutil
import time
import matplotlib.pyplot as plt

script_name = "keylogger.py"
pid = None

# Try to find a running Python process that includes 'keylogger.py'
for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
    try:
        cmdline = proc.info.get('cmdline')
        if cmdline and any(script_name in arg for arg in cmdline):
            pid = proc.info['pid']
            print(f"Found running keylogger with PID: {pid}")
            break
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        continue

if pid is None:
    print("Keylogger script not running. Start it first.")
    exit()

# Now track memory usage
process = psutil.Process(pid)
memory_usage = []
time_axis = []

print("Tracking memory usage for 30 seconds...")

for t in range(30):
    mem = process.memory_info().rss / (1024 * 1024)  # MB
    memory_usage.append(mem)
    time_axis.append(t)
    print(f"Time: {t}s → Memory: {mem:.2f} MB")
    time.sleep(1)

# Plotting
plt.plot(time_axis, memory_usage, color='green', marker='o')
plt.xlabel('Time (seconds)')
plt.ylabel('Memory Usage (MB)')
plt.title('Memory Usage Over Time (Keylogger)')
plt.grid(True)
plt.tight_layout()
plt.show()
