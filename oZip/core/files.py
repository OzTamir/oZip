from util import *
from Compression.base import CompressionEngine
from Compression.huffman import *
import binascii

class FilesCompressor(CompressionEngine):
	def __init__(self):
		CompressionEngine.__init__(self, 'Files compressor')

	def compress(self, filename):
		''' Compression function for any non-text file '''
		compressor = HuffmanCompressor()

		with open(filename, 'rb') as file:
			data = file.read()
		data = binascii.hexlify(data)
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
		decomp = decompressor(str_data)
		decomp = binascii.unhexlify(decomp)
		new_filename = '.'.join(filename.split('.')[:2])
		with open(new_filename, 'wb') as file:
			file.write(decomp)
