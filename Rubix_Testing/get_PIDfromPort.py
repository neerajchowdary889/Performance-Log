import subprocess
import re

def get_pid_from_port(port):
    command = f'sudo netstat -nlp | grep :{port}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        return (None, False)
    matches = re.search(r'LISTEN\s+(\d+)/', stdout.decode())
    if matches:
        return (int(matches.group(1)), True)
    else:
        return (None, False)


if __name__ == '__main__':
    port = 20009
    try:
        pid = get_pid_from_port(port)
        if pid[1] == True:
            print(pid[0])
        else:
            print(0)
    except:  
        print(0)