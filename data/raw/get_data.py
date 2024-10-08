from spacetrack import SpaceTrackClient
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('SPACETRACK_USERNAME')
password = os.getenv('SPACETRACK_PASSWORD')

st = SpaceTrackClient(username, password)
tle_data = st.tle_latest(norad_cat_id=[25544, 41335], ordinal=1, format='tle')
print(tle_data)

with open('data/raw/tle_data.tle', 'w') as tle_file:
    tle_file.write(tle_data)