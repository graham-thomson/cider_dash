import os
import glob
import re
import requests
import subprocess


def to_temp_f(x):
    return float(x) * (9./5.) + 32.


def get_cpu_temp():

    return to_temp_f(float(re.search(r"(\d{2,}.\d+)",
                                     subprocess.check_output("vcgencmd measure_temp", shell=True)).group()))


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


def get_probe_temp():
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

    with open(device_file, "r") as f:
        lines = f.readlines()
        if lines[0].strip()[-3:] == "YES":
            temp_str = re.search(r"(t=)(\d{5,})", lines[1])
            if temp_str:
                return to_temp_f(int(temp_str.groups()[1])/1000)
    return None
