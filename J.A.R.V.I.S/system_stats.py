from psutil import cpu_percent,sensors_battery,virtual_memory
from Speak import Speak

def getcpuper(percpu=False):
    if percpu:
        cpu_say="The usages of cpu cores are "
        for x in cpu_percent(interval=1,percpu=percpu):
            cpu_say+=str(x)+", "
        cpu_say+="percent respectively"
    else:
        cpu_say="CPU usage is "+str(cpu_percent(interval=1,percpu=percpu))+" percent"
    # return cpu_say
    Speak(cpu_say)

def getbattery():
    battery_say=""
    battery=sensors_battery()
    battery_say+=str(battery.percent)+" percent power left. "
    if battery.percent<30 and (not battery.power_plugged):
        battery_say+="running on emergency backup power. approximately "+str(battery.secsleft/60)+" minutes remaining."
    elif not battery.power_plugged:
        battery_say+=" approximately "+str(int(battery.secsleft/60))+" minutes remaining."
    else:
        battery_say+="plugged in, charging"
    Speak(battery_say)

def getram():
    ram_say="System memory usage is "
    memory=virtual_memory()
    ram_say+=str(memory.percent)+" percent."
    if memory.percent>85:
        ram_say+=" System overload detected."
    else:
        ram_say+=" No overload detected"
    Speak(ram_say)

