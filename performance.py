#!/usr/bin/python3
import subprocess

Details = {}

# print("Temperature")
try:
  temp=int(subprocess.check_output("cat /sys/class/thermal/thermal_zone0/temp", shell=True))
  temp=temp/1000  
  Details["Temp"] = temp
  # print('>>>',temp)
except:
  Details["Temp"] = None
  raise Exception("Temperatures Something went wrong")


# print("Available-RAM")
try:
  RAM=int(subprocess.check_output("free | awk 'NR==2 {print $7}'",shell=True))
  RAM=round(RAM/1024, 3)
  Details["RAM"] = RAM
  # print(f'>>> {RAM} MB')
except:
  Details["RAM"] = None
  raise Exception("RAM Something went wrong")


# print("CPU usage")
try:
  CPU=float(subprocess.check_output("top -n1 | awk '/Cpu\(s\):/ {print $2}'",shell=True))
  Details["CPU"] = CPU
  # print(f'>>> {CPU}%')
except:
    Details["CPU"] = None
    raise Exception("CPU Something went wrong")


# print("Disk Usage")
try:
  disk=subprocess.check_output("df -h --total | awk 'NR==11 {print $5}'",shell=True)
  # print(disk)
  disk=float(disk[:2])
  Details["Disk"] = disk
  # print(f'>>> {disk}%')
except:
    disk=0
    Details["Disk"] = None
    raise Exception("Disk Usage Something went wrong")


print(Details)