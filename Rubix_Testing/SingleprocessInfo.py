import psutil
import threading
from get_PIDfromPort import get_pid_from_port
import time
import itertools
import sys

def get_process_stats(pid):
    process = psutil.Process(pid)
    memory_info = process.memory_info()
    cpu_percent = process.cpu_percent(interval=1.0)
    return memory_info.rss, cpu_percent

def process(pid, logfile):
    try:
        ram_usage, cpu_usage = get_process_stats(pid)
        details = {
            'Process ID': pid,
            'RAM usage': round(ram_usage / (1024 * 1024),2), # In MB
            'CPU usage': cpu_usage # In %
        }
    except:
        details = {'Error': "Smart Contract deployment not yet started..."}
    
    with open(logfile, 'a') as f:
        f.write(str(details) + '\n')

port_logfile_map = {
    20000: "Log/LogPort1.log",
    20001: "Log/LogPort2.log",
    20002: "Log/LogPort3.log",
    20003: "Log/LogPort4.log",
    20004: "Log/LogPort5.log",
    20005: "Log/LogPort6.log",
    20006: "Log/LogPort7.log",
    20007: "Log/LogPort8.log",
    20008: "Log/LogPort9.log",
    20009: "Log/LogPort10.log",
}

spinner = itertools.cycle(['-', '/', '|', '\\'])
port_pid_map = {}

for port, logfile in port_logfile_map.items():
    pid = get_pid_from_port(port)
    print(pid)
    port_pid_map[port] = pid[0]

while True:
    threads = []
    for port, logfile in port_logfile_map.items():
        pid = port_pid_map[port]
        if pid == 0:
            with open(logfile, 'a') as f:
                f.write("{'Error': 'pid not found...'}\n")
        else:
            thread = threading.Thread(target=process, args=(pid, logfile))
            thread.start()
            threads.append(thread)

    while any(thread.is_alive() for thread in threads):
        sys.stdout.write(next(spinner))  # write the next character
        sys.stdout.flush()  # flush stdout buffer (actual character display)
        sys.stdout.write('\b')  # erase the last written character
        time.sleep(0.1)

    for thread in threads:
        thread.join()

    time.sleep(1) 