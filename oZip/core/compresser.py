class Compresser(object):
	"""Base class for Compressers"""
	def __init__(self, compress_type='Non-defined'):
		super(Compresser, self).__init__()
		self.type = compress_type
		self.compression = None

	def __repr__(self):
		return 'Compresser of type %s.' % str(self.type)

	def setup(self, compression_function, new_type=None):
		''' Setup the compression functionality based on the compression type '''
		self.compression = compression_function
		if new_type:
			self.type = new_type

	def compress(self, data):
		''' Apply the compression '''
		if self.compression is None:
			raise ValueError('No compression defined.')
		else:
			return self.compression(data)


		