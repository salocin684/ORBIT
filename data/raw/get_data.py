# Imports
import skyfield.api as skyapi
from tletools import TLE

# Load data
loader = skyapi.Loader(r"C:\\Users\\Nicolas\\Documents\\Projecten\\ORBIT\\data\\raw\\")
active_satellites_url = 'tle_data.tle'
satellites = loader.tle(active_satellites_url)

#print(satellites.keys())
#print(satellites.values())
#print(satellites.items())
#print(type(satellites))

#k, v = satellites.items()




#satellites = load.tle(lines)
#print(satellites)

# Calculate its position at the current time
#ts = load.timescale()
#t = ts.now()
#geocentric = satellites.at(t)

# Earth ground based location
#subpoint = geocentric.subpoint()
#print('Latitude:', subpoint.latitude.degrees)
#print('Longitude:', subpoint.longitude.degrees)