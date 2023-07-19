# CMD Line Assignment

This Python command line program calculates the average of air pollutant PM2.5 over n minutes, of
all the stations that are map bound by two pairs of latitudes and longitudes.

The program retrieves data from the JSON API at https://aqicn.org/json-api/doc/.

The command line program takes:
- coordinates that would represent a map bound: lat_1, lng_1,
lat_2, lng_2
- sampling period in minutes (default = 5)
- sampling rate in sample(s) / minute (default = 1)

Run in the terminal as: `python cmd-line-assn.py "lat_1,lng_1,lat_2,lng_2" period rate`
