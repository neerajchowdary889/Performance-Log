import subprocess

try:
    cmd = 'ps -ef | grep truffle'
    output = subprocess.check_output(cmd, shell=True).decode('utf-8')

    output_lines = output.splitlines()

    process_ids = []

    # Extracting process IDs
    for line in output_lines:
        parts = line.split()
        if len(parts) > 1:
            process_id = parts[1]
            process_ids.append(process_id)

    # Printing the process IDs
    Truffle_PID = process_ids[2]
except:
    Truffle_PID = 0