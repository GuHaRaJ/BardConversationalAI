from psutil import cpu_percent, sensors_battery, virtual_memory
from Speak import Speak

def getbattery():
	battery_say = ""
	battery = sensors_battery()
	battery_say += str(battery.percent) + " percent power left. "
	if battery.percent < 30 and (not battery.power_plugged):
		battery_say += "running on emergency backup power. approximately " + str(
			battery.secsleft / 60) + " minutes remaining."
	elif not battery.power_plugged:
		battery_say += " approximately " + str(int(battery.secsleft / 60)) + " minutes remaining."
	else:
		battery_say += "plugged in, charging"
	Speak(battery_say)
	return battery_say

