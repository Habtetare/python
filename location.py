import sys

def main():
    coordinates_tulip = (45.376,-71.115)
    coordinates_list = [45.376,-71.115]
    latitude,longtiude = coordinates_tulip
    #print(f"Latitude: {coordinates_tulip[0]}")
    #print(f"Longitude: {coordinates_tulip[1]}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longtiude}")
    print(f"{sys.getsizeof(coordinates_tulip)} bytes")
    print(f"{sys.getsizeof(coordinates_list)} bytes")
main()
