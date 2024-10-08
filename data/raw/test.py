from spacetrack import SpaceTrackClient
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('SPACETRACK_USERNAME')
password = os.getenv('SPACETRACK_PASSWORD')

from spacetrack import SpaceTrackClient
st = SpaceTrackClient(username, password)