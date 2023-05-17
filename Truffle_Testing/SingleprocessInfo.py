import psutil
from get_PID import Truffle_PID

Details = {}

def get_process_stats(pid):
    process = psutil.Process(pid)
    memory_info = process.memory_info()
    cpu_percent = process.cpu_percent(interval=1.0)
    return memory_info.rss, cpu_percent

def process(pid):
    try:
        ram_usage, cpu_usage = get_process_stats(pid)

        Details['Process ID'] = pid
        Details['RAM usage'] = round(ram_usage / (1024 * 1024),2) # In MB
        Details['CPU usage'] = cpu_usage # In %
    except:
        Details['Error'] = "Smart Contract deployment not yet started..."

pid = int(Truffle_PID)
if pid == 0:
    Details['Error'] = "Truffle not found..."
else:
    process(pid)
    
print(Details)