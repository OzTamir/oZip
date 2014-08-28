from heapq import heappush, heappop, heapify
from collections import Counter
import json

def create_tree(data):
	''' Create huffman encoding for a given string '''
	heap = [[wt, [sym, ""]] for sym, wt in Counter(data).items()]
	heapify(heap)
	while len(heap) > 1:
		lo = heappop(heap)
		hi = heappop(heap)
		for pair in lo[1:]:
			pair[1] = '0' + pair[1]
		for pair in hi[1:]:
			pair[1] = '1' + pair[1]
		heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
	return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def create_encode_dict(code):
	encode = dict()
	for char in code:
		encode[char[0]] = char[1]
	return encode

def build_decode_dict(encoding_dict):
	return {y : x for x, y in encoding_dict.items()}

def get_decoding_dict(data):
	chars_to_read = int(data[:32], 2)
	data_start = 32 + chars_to_read
	decode_json = data[32: data_start]
	decode_json = [decode_json[16 * i : 16 * (i + 1)] for i in range(len(decode_json) / 16)]
	decode_str = []
	for i in decode_json:
		decode_str.append(chr(int(i[-8:], 2)))
	decode_str = ''.join(decode_str)
	try:
		return json.loads(decode_str), data_start
	except UnicodeDecodeError:
		return json.loads(decode_str), data_start

