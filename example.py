from oZip.core.util import *
from oZip.core.Huffman.huffman import *
comp = HuffmanCompressor()
deco = HuffmanDecompressor()

# Compressing
with open('demo.png', 'rb') as file:
	data = file.read().decode("UTF8")

compressed = comp(data)
bin_str = str2bin(compressed)
with open('demo.ozip', 'wb') as file:
	file.write(bin_str)


# Decompressing
with open('demo.ozip', 'rb') as file:
	data = file.read()

str_data = bin2str(data)
decomp = deco(str_data).encode("UTF8")

with open('demo2.png', 'wb') as file:
	file.write(decomp)
