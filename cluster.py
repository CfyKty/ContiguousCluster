import math,json

try:
    with open('config.json', 'r') as f:
        config = json.load(f)

    cluster_size = int(config['cluster'])
    sector_size = int(config['sector'])
    FAT_start = int(config['fat_start'])

    bytes_per_cluster = int(config['bytes_per_cluster'])
    EOF = ("F"*bytes_per_cluster) #EOF marker.

except FileNotFoundError:
    cluster_size = int(input("Enter cluster size: "))
    EOF = "FFFFFFFF"

start = int(input("Enter start: "), 16)
size = int(input("Enter size: "), 16)

cluster = ""
clusters_to_write = math.ceil(size / cluster_size)
print("\n Writing "+clusters_to_write+"clusters.")

FAT_location = FAT_start * sector_size #fat 32 964 * 512
address = (start * bytes_per_cluster) + FAT_location

for outp in range(start + 1, start + clusters_to_write):
    ba = bytearray.fromhex("{0:08x}".format(outp)) #converts to hex byte array
    ba.reverse() 									#endian-ness
    hexdigit = ''.join(format(x, '02x') for x in ba)  # constructs hex number from byte array
    cluster += hexdigit.upper()							#formats hex "Letters"

print("\nPaste at address: 0x"+address+"\n")
print(cluster + EOF)
