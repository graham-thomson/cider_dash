import re
import requests
import subprocess

to_temp_f = lambda x: float(x) * (9./5.) + 32.

def get_cpu_temp():
    return to_temp_f(float(re.search(r"(\d{2,}.\d+)", subprocess.check_output("vcgencmd measure_temp", shell=True)).group()))

def calibrated_temp(sh):
    sh_temp = to_temp_f(sh.get_temperature())
    cpu_temp = get_cpu_temp()
    return (0.6816715 * sh_temp) + (0.11538254 * cpu_temp) + 2.839289281005719

def get_inside_temp(sh):
    return to_temp_f(sh.get_temperature())

def get_outside_temp(apikey, lat, long):
    try:
        r = requests.get("https://api.darksky.net/forecast/{key}/{lat},{long}".format(key=apikey, lat=lat, long=long))
        if r.status_code == 200:
            outside_temp = r.json()["currently"]["temperature"]
            try:
                outside_temp = float(outside_temp)
                return outside_temp
            except (ValueError, TypeError):
                return None
        return None
    except:
        return None