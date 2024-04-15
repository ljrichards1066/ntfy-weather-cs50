import requests
import json
import sys
import re




def main():
    mdict = {"zip":None,"ip":None,"hour":None,"longitude":None,"city":None,"latitude":None,"high":None,"low":None,"precip":None,"final":None}
    #test_url_and_api()
    mdict = input_verify(mdict)
    mdict = zip_to_location(mdict)
    mdict = zip_to_time(mdict)
    mdict = call_weather(mdict)
    mdict = format_string(mdict)
    push_ntfy(mdict)



def input_verify(mdict):
    if len(sys.argv) != 3:
        print("Incorrect number of command line arguments")
        sys.exit(1)
    matches = re.search(r"^[0-9][0-9][0-9][0-9][0-9]$", sys.argv[1])
    if not matches:
        print("Incorrectly formatted zip")
        sys.exit(1)
    matches2 = re.search(r"^https?://.+/.+$", sys.argv[2])
    if not matches2:
        print("Incorrectly formatted URL or IP. Please be sure to include HyperText Transfer Protocol and the topic.")
        sys.exit(1)
    mdict.update({"zip":sys.argv[1]})
    mdict.update({"ip":sys.argv[2]})
    return mdict
def zip_to_location(mdict):
    #Call api
    response = requests.get("http://api.zippopotam.us/us/" + mdict["zip"])
    raw = response.json()
    if response.status_code != 200:
        print("There was a problem connecting to one or more required APIs. Please check network connection and try again or check that the Zip Code entered is valid")
        sys.exit(0)
    #o = json.loads(response.text)
    #p = json.dumps(o, indent=2)
    #print(p)
    try:
        lonraw = ((raw["places"][0]["longitude"]))
        latraw = ((raw["places"][0]["latitude"]))
        longitude = str(round(float(lonraw), 2))
        latitude = str(round(float(latraw), 2))
        city = ((raw["places"][0]["place name"]))
        mdict.update({"longitude":longitude})
        mdict.update({"latitude":latitude})
        mdict.update({"city":city})
    except KeyError:
        print("Something went wrong, please check your connection or check that the Zip Code entered is valid.")
        sys.exit(1)
    return mdict

def zip_to_time(mdict):
    #Call api
    response = requests.get("https://timeapi.io/api/Time/current/coordinate?latitude=" + mdict["latitude"] + "&longitude=" + mdict["longitude"])
    raw = response.json()
    if response.status_code != 200:
        print("There was a problem connecting to one or more required APIs. Please check network connection and try again.")
        sys.exit(0)
    #o = json.loads(response.text)
    #p = json.dumps(o, indent=2)
    hour = (raw["hour"])
    mdict.update({"hour":hour})
    return mdict
def call_weather(mdict):
    #Call api
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=" + mdict["latitude"] + "&longitude=" + mdict["longitude"] + "&hourly=temperature_2m,precipitation_probability,precipitation&daily=temperature_2m_max,temperature_2m_min&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=auto&forecast_days=1")
    raw = response.json()
    if response.status_code != 200:
        print("There was a problem connecting to one or more required APIs. Please check network connection and try again.")
        sys.exit(0)
    #o = json.loads(response.text)
    #p = json.dumps(o, indent=2)
    #print(p)
    precip_list = (raw["hourly"]["precipitation_probability"])
    chance = 0
    for hour in precip_list[(mdict["hour"]):]:
        if (int(hour)) > chance:
            chance = hour
    mdict.update({"high":((raw["daily"]["temperature_2m_max"])[0])})
    mdict.update({"low":(raw["daily"]["temperature_2m_min"])[0]})
    mdict.update({"precip":(str(chance) + "%")})
    return mdict

def format_string(mdict):
     mdict.update({"final":(f'The high in {(mdict["city"])} is {(mdict["high"])}°F and the low is {(mdict["low"])}°F. There is a {(mdict["precip"])} chance of precipitation for the rest of the day.')})
     return mdict
def push_ntfy(mdict):
    requests.post(mdict["ip"],
        data=(mdict["final"]).encode(encoding='utf-8'))
    print(f'Sent following string to Ntfy server, {mdict["ip"]}. If it did not go through, please confirm the address and that the topic is listed, I.E "https://ntfy.sh/mytopic".\n{mdict["final"]}')


if __name__ == "__main__":
    main()