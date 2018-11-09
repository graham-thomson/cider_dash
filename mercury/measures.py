import re
import requests
import subprocess

to_temp_f = lambda x: float(x) * (9./5.) + 32.

def cpu_temp():
    return to_temp_f(float(re.search(r"(\d{2,}.\d+)", subprocess.check_output("vcgencmd measure_temp", shell=True)).group()))

def calibrated_temp(sh):
    temp = to_temp_f(sh.get_temperature())
    return temp - ((cpu_temp() - temp)/.7)

def get_inside_temp(sh):
    return to_temp_f(sh.get_temperature())

def get_outside_temp(apikey, lat, long):
    try:
        r = requests.get("https://api.darksky.net/forecast/{key}/{lat},{long}".format(key=apikey, lat=lat, long=long))
        if r.status_code == 200:
            return r.json()["currently"]["temperature"]
        return None
    except:
        return None