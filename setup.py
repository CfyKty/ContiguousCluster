import json

root = int(input("Enter base10 root directory start: "))
reserved = int(input("Enter reserved :"))
cluster_size = int(input("Enter cluster size :"))
sector_size = int(input("Enter sector size :"))

config = {'reserved': reserved, 'root': root, 'cluster': cluster_size, 'sector': sector_size}

with open('config.json', 'w') as f:
    json.dump(config, f)
