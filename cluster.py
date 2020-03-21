import math
start = int(input("Enter start: "),16)
size = int(input("Enter size: "),16)
cluster ="" 
clusters_to_write = math.ceil(size/0x1000)
print(clusters_to_write)
for outp in range(start+1,start+(clusters_to_write)):
	ba = bytearray.fromhex("{0:08x}".format(outp))
	ba.reverse()
	str = ''.join(format(x,'02x') for x in ba)
	cluster+=str.upper()

print(cluster)


