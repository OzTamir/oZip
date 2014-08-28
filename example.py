from oZip.core.util import *
from oZip.core.Huffman.huffman import *

comp = HuffmanCompressor()
deco = HuffmanDecompressor()

# Compressing
with open('tmp.txt', 'rb') as file:
	data = file.read()

compressed = comp(data)
bin_str = str2bin(compressed)
with open('tmp.ozip', 'wb') as file:
	file.write(bin_str)


# Decompressing
with open('tmp.ozip', 'rb') as file:
	data = file.read()

str_data = bin2str(data)
decomp = deco(str_data)

with open('tmp2.txt', 'wb') as file:
	file.write(decomp)
