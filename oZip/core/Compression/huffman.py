from base import Compressor, Decompressor
from huffman_utils import *

class HuffmanCompressor(Compressor):
	def __init__(self):
		Compressor.__init__(self)

	def compress(self, data):
		''' Compress data using Huffman code '''
		try:
			assert isinstance(data, str) or isinstance(data, unicode)
		except AssertionError, e:
			raise TypeError('Data should be string, but is %s.' % str(type(data)))
		# Create the Huffman code
		code = create_tree(data)
		# Create encoding dictionary
		encoding = create_encode_dict(code)
		# Create the compressed data
		compressed = ''.join(encoding[val] for val in data)
		# Create the decoding dictionary
		decode_dict = build_decode_dict(encoding)
		# Convert the decoding dictionary to json so we can add it
		try:
			json_decode = json.dumps(decode_dict).replace(' ', '')
		except UnicodeDecodeError:
			json_decode = json.dumps(decode_dict, ensure_ascii=False).replace(' ', '')
		# Convert the decode dict to binary string
		bin_json = ''.join('{:016b}'.format(int(bin(ord(i))[2:], 2)) for i in json_decode)
		# Add a 32bit prefix to tell the decompressor the length of the decoding dict.
		prefix = '{:032b}'.format(len(bin_json))
		return ''.join([prefix, bin_json, compressed])

class HuffmanDecompressor(Decompressor):
	''' Decompress a Huffman-code-compressed data '''
	def __init__(self):
		Decompressor.__init__(self)
	
	def decompress(self, data):
		try:
			assert isinstance(data, str) or isinstance(data, unicode)
		except AssertionError, e:
			raise TypeError('Data should be string, but is %s.' % str(type(data)))
		# Get the decoding dictionary and the starting point of the actual data
		decode, start = get_decoding_dict(data)
		# Initialize variables
		result = []
		prefix = ''
		# Decode the compressed data
		for bit in data[start:]:
			# Add the next bit to the prefix
			prefix += bit
			# If it's not in the decoding dict, go on and expand the prefix
			if prefix not in decode:
				continue
			# If it is, check if it's an empty string (the spaces are removed, so if theres an empty
			# string in the decoding dictionary it's the space char
			decoded = decode[prefix]
			# If it is, replace it to the actual char
			if decoded == '':
				decoded = ' '
			# Add it to the final result
			result.append(decoded)
			# Reset the prefix
			prefix = ''
		# The prefix should be an empty string at this point
		try:
			assert prefix == ''
		except AssertionError, e:
			# Due to padding, sometimes the leftovers are a char that lost some of it's 0 prefix
			for i in range(8 - len(prefix)):
				prefix = '0' + prefix
				# Add 0 to the prefix, and check if its in the decoding dict
				if prefix in decode:
					# If it is, NOW we can return
					result.append(decode[prefix])
					prefix = ''
					break
			if prefix != '':
				raise ValueError('Decompression process finished with leftovers.')
		# If everything is good, return the decompressed data
		return ''.join(result)