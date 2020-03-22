import math,json

try:
    with open('config.json', 'r') as f:
        config = json.load(f)

    cluster_size = int(config['cluster'])

except FileNotFoundError:
    cluster_size = int(input("Enter cluster size: "))

start = int(input("Enter start: "), 16)
size = int(input("Enter size: "), 16)

cluster = ""
clusters_to_write = math.ceil(size / cluster_size)
print(clusters_to_write)

for outp in range(start + 1, start + clusters_to_write):
    ba = bytearray.fromhex("{0:08x}".format(outp)) #converts to hex byte array
    ba.reverse() 									#endian-ness
    hexdigit = ''.join(format(x, '02x') for x in ba)  # constructs hex number from byte array
    cluster += hexdigit.upper()							#formats hex "Letters"

print(cluster)
