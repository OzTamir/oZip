from utils import *
from ..base import Compressor, Decompressor

class HuffmanCompressor(Compressor):
	"""docstring for HuffmanCompressor"""
	def __init__(self):
		Compressor.__init__(self)

	def compress(self, data):
		try:
			assert isinstance(data, str) or isinstance(data, unicode)
		except AssertionError, e:
			raise TypeError('Data should be string, but is %s.' % str(type(data)))
		code = create_tree(data)
		encoding = create_encode_dict(code)
		compressed = ''.join(encoding[val] for val in data)
		decode_dict = build_decode_dict(encoding)
		json_decode = json.dumps(decode_dict).replace(' ', '')
		print 'Decode dict len: %s' % str(len(json_decode))
		# Convert the decode dict to binary string
		bin_json = ''.join('{:016b}'.format(int(bin(ord(i))[2:], 2)) for i in json_decode)
		# Add a 32bit prefix to tell the decompressor the length of the decoding dict.
		prefix = '{:032b}'.format(len(bin_json))
		return ''.join([prefix, bin_json, compressed])

class HuffmanDecompressor(Decompressor):
	"""docstring for HuffmanDecompressor"""
	def __init__(self):
		Decompressor.__init__(self)
	
	def decompress(self, data):
		decode, start = get_decoding_dict(data)
		result = []
		prefix = ''
		for bit in data[start:]:
			prefix += bit
			if prefix not in decode:
				continue
			decoded = decode[prefix]
			if decoded == '':
				decoded = ' '
			result.append(decoded)
			prefix = ''
		assert prefix == ''
		return ''.join(result)