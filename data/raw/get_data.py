from spacetrack import SpaceTrackClient
from dotenv import load_dotenv
import os
import time

load_dotenv()

username = os.getenv('SPACETRACK_USERNAME')
password = os.getenv('SPACETRACK_PASSWORD')

st = SpaceTrackClient(username, password)
#tle_data = st.tle_latest(norad_cat_id=[int('00011'), 61447], ordinal=1, format='tle')
#print(tle_data)

norad_cat_ids = list(range(11, 61448))

os.makedirs('data/raw', exist_ok=True)

with open('data/raw/tle_data.tle', 'w') as tle_file:
    batch_size = 128
    for i in range(0, len(norad_cat_ids), batch_size):
        batch_ids = norad_cat_ids[i:i + batch_size]
        try:
            tle_data = st.tle_latest(norad_cat_id=batch_ids, ordinal=1, format='tle')
            print(f"Fetched data for batch {i // batch_size + 1}: NORAD IDs {batch_ids[0]} to {batch_ids[-1]}")
            
            tle_file.write(tle_data + '\n')
            
            time.sleep(1)
        except Exception as e:
            print(f"Error fetching data for batch {i // batch_size + 1}: {e}")
            continue