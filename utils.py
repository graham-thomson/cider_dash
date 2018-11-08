import requests

def get_outside_temp(apikey, lat, long):
    request_url = "https://api.darksky.net/forecast/{key}/{lat},{long}".format(key=apikey, lat=lat, long=long)
    print(request_url)
    r = requests.get(request_url)
    if r.status_code == 200:
        return r.json()["currently"]["temperature"]
    return None
