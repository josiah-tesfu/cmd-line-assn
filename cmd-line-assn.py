import argparse
import requests
import time

token = "1327fb6351f3b16cc0ad6659b17a74a5f890d27b"

# Add the cmd line arguments
parser = argparse.ArgumentParser()
parser.add_argument("latlng", type=str)
parser.add_argument("period", nargs = "?", type=int, default=5)
parser.add_argument("rate", type=int, nargs = "?", default=1)

# Parse the cmd line arguments
args = parser.parse_args()
interval = 60.0 / args.rate
period = args.period * 60

# Get the ID's for all the stations given by latlng
stations_list_response = requests.get(f"https://api.waqi.info/v2/map/bounds?latlng={args.latlng}&networks=all&token={token}").json()
uid_list = [data["uid"] for data in stations_list_response["data"]]

start_time = time.time()

# continue getting response data until the period has elapsed
while time.time() - start_time <= period:

    # Get pm25 values for all cities at a single time:
    pm25_list = []
    for uid in uid_list:
        station_feed_response = requests.get(f"https://api.waqi.info/feed/@{uid}/?token={token}").json()
        # Some station feed responses don't have a pm25 recording
        if "pm25" not in station_feed_response["data"]["iaqi"]:
            continue
        pm25 = station_feed_response["data"]["iaqi"]["pm25"]["v"]
        pm25_list.append(pm25)
        # Print PM2.5 sampled value
        print(f"PM2.5 value for station {uid}: {pm25}")

    time.sleep(interval)

# Print overall PM2.5 average of all stations over n minutes of sampling
average_pm25 = sum(pm25_list) / len(pm25_list)
print(f"Overall PM2.5 average over {args.period} minutes: {average_pm25:.3f}")