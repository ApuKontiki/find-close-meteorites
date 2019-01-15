import math
import requests

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    alpha = (lat2 - lat1) / 2
    beta = (lon2 - lon1) / 2

    h = math.sin(alpha)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(beta)**2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

def get_dist(meteor):
    return meteor.get('distance', math.inf)

if __name__ == '__main__':
    my_loc = (29.424122, -98.493628)

    meteor_response = requests.get('https://data.nasa.gov/resource/y77d-th95.json')
    meteor_data = meteor_response.json()

    for meteor in meteor_data:
        if ('reclat' in meteor and 'reclong' in meteor):
            lat1 = float(meteor['reclat'])
            lon1 = float(meteor['reclong'])
            lat2 = my_loc[0]
            lon2 = my_loc[1]
            meteor['distance'] = calc_dist(lat1, lon1, lat2, lon2)

    meteor_data.sort(key = get_dist)

    print(meteor_data[0:10])
