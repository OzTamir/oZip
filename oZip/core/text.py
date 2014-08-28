from util import *
from Compression.base import CompressionEngine
from Compression.huffman import *

class TextCompressor(CompressionEngine):
	def __init__(self):
		CompressionEngine.__init__(self, 'Text compressor')

	def compress(self, filename):
		''' Compression function for any non-text file '''
		compressor = HuffmanCompressor()

		with open(filename, 'rb') as file:
			data = file.read().decode("UTF8")
		compressed = compressor(data)
		bin_str = str2bin(compressed)
		new_filename = filename + '.ozip'
		with open(new_filename, 'wb') as file:
			file.write(bin_str)

	def decompress(self, filename):
		# Decompressing
		decompressor = HuffmanDecompressor()
		with open(filename, 'rb') as file:
			data = file.read()
		str_data = bin2str(data)
		decompressed = decompressor(str_data).encode("UTF8")
		new_filename = '.'.join(filename.split('.')[:2])
		with open(new_filename, 'wb') as file:
			file.write(decompressed)