# --- String and binary utilities --- #
def str2bin(data):
	''' Convert a string into a binary format '''
	temp = None
	# Add padding if there isn't flat 8-bit
	if len(data) % 8 != 0:
		temp = data[-(len(data) % 8):]
	data = [data[8 * i : 8 * (i + 1)] for i in range(len(data) / 8)]
	if temp:
		data.append(temp)
	data = [int(i, 2) for i in data]
	data = ''.join(chr(i) for i in data)
	return data

def bin2str(data):
	''' Read a binary string into decompressable format '''
	data = [ord(i) for i in data]
	data = ['{:08b}'.format(int(bin(i), 2)) for i in data]
	# We need to remove the padding we've added in the str2bin function
	# If there isn't padding, we remove some of the prefix but it's fine as
	# we restore it in the Huffman decompress function.
	temp = data[-1]
	while temp[0] == '0':
		temp = temp[1:]
	data[-1] = temp
	return ''.join(data)

