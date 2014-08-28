class CompressionEngine(object):
	"""Base class for Compression Engines"""
	def __init__(self, compress_type='Non-defined'):
		self.type = compress_type
		self.compressor = None
		self.decompressor = None

	def __repr__(self):
		return 'Compresser of type %s.' % str(self.type)

	def setup(self, compressor, decompressor):
		''' Setup the compression functionality based on the compression type '''
		self.compressor = compressor
		self.decompressor = decompressor

	def compress(self, data):
		''' Apply the compression '''
		if self.compressor is None:
			raise ValueError('No compression defined.')
		else:
			return self.compressor(data)

	def decompress(self, compressed_data):
		''' Apply the decompression '''
		if self.decompressor is None:
			raise ValueError('No compression defined.')
		else:
			return self.decompressor(compressed_data)

class Compressor(object):
	"""Base class for Compressors"""
	def __init__(self):
		super(Compressor, self).__init__()

	def compress(self, data):
		return data

	def __call__(self, data):
		return self.compress(data)

class Decompressor(object):
	"""Base class for Decompressor"""
	def __init__(self):
		super(Decompressor, self).__init__()

	def decompress(self, data):
		return data

	def __call__(self, data):
		return self.decompress(data)



















