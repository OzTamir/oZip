# --- String and binary utilities --- #
def str2bin(data):
	''' Convert a string into a binary format '''
	data = [data[8 * i : 8 * (i + 1)] for i in range(len(data) / 8)]
	data = [int(i, 2) for i in data]
	data = ''.join(chr(i) for i in data)
	return data

def bin2str(data):
	''' Read a binary string into decompressable format '''
	data = [ord(i) for i in data]
	data = ''.join(['{:08b}'.format(int(bin(i), 2)) for i in data])
	return data

