import json
import sys

try:
    with open('config.json', 'r') as f:
        config = json.load(f)

    reserved = int(config['reserved'])
    start = int(config['start'])
    cluster_size = int(config['cluster'])
    sector_size = int(config['sector'])

except FileNotFoundError:
    start = int(input("Enter base10 custer area start: "))
    reserved = int(input("Enter reserved: "))
    cluster_size = int(input("Enter cluster size: "))
    sector_size = int(input("Enter sector size: "))

clusters_per_sector = cluster_size/sector_size

escaped = False

while not escaped:
    location = input("Enter location: 0x")
    if location.lower() == "q":
        escaped = True
        sys.exit()
    else:
        location = int(location, 16)
        absolute_location = (((location - reserved) * clusters_per_sector) + start) * sector_size
        print(hex(int(absolute_location)))
