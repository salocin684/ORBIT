from sgp4.api import Satrec, jday
from datetime import datetime, timedelta, timezone

tle_file_path = 'data/raw/tle_data.tle'

def read_tle_file(tle_file_path):
    with open(tle_file_path, 'r') as f:
        lines = f.readlines()

    tle_pairs = [(lines[i], lines[i+1]) for i in range(0, len(lines), 2)]
    return tle_pairs

tle_pairs = read_tle_file(tle_file_path)
tle_line1, tle_line2 = tle_pairs[0]  
satellite = Satrec.twoline2rv(tle_line1.strip(), tle_line2.strip())

def propagate_debris_to_time(satellite, year, month, day, hour, minute, second):
    jd, fr = jday(year, month, day, hour, minute, second)
    e, r, v = satellite.sgp4(jd, fr)  # r = position (km), v = velocity (km/s)
    
    if e == 0:
        return r  # Return position (x, y, z in km)
    else:
        print(f"Error in propagation with code: {e}")
        return None

start_time = datetime.now(timezone.utc)
positions = []

# Track the debris over the next 24 hours at 1-hour intervals
for i in range(24):
    current_time = start_time + timedelta(hours=i)
    position = propagate_debris_to_time(satellite, current_time.year, current_time.month, current_time.day,
                                        current_time.hour, current_time.minute, current_time.second)
    if position:
        positions.append((current_time, position))
        print(f"Time: {current_time}, Position: {position}")
