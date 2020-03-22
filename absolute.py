import json

with open('config.json', 'r') as f:
    config = json.load(f)

reserved = config['reserved']
root = config['root']

location = int(input("Enter location :0x"), 16)


absolute_location = ((location - reserved) * 8) + root

print(absolute_location)
