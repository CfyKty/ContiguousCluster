import json

fat_start = int(input("Enter FAT start: "))
bytes_per_cluster = int(input("Enter bytes used per cluster (4 for FAT32): "))
start = int(input("Enter base10 cluster area start: "))
reserved = int(input("Enter reserved (2 for FAT32): "))
cluster_size = int(input("Enter cluster size: "))
sector_size = int(input("Enter sector size: "))

config = {'fat_start':fat_start,'bytes_per_cluster':bytes_per_cluster,'reserved': reserved,'start': start, 'cluster': cluster_size, 'sector': sector_size}

with open('config.json', 'w') as f:
    json.dump(config, f)
