import yaml
from spacetrack import SpaceTrackClient

with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

username = config['SPACETRACK_USERNAME']
password = config['SPACETRACK_PASSWORD']
st = SpaceTrackClient(username, password)