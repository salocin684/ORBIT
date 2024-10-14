# Unit tests for debris tracking and position calculations
import numpy as np

earth_radius = 6378.1

x, y, z = -7558.241700805863, -87.60046586808127, -3851.315361868448

altitude = np.sqrt(x**2 + y**2 + z**2) - earth_radius
longitude = np.degrees(np.arctan2(y, x))
latitude = np.degrees(np.arcsin(z / np.sqrt(x**2 + y**2 + z**2)))

print(f"Latitude: {latitude}, Longitude: {longitude}, Altitude: {altitude} km")
