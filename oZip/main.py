from core.text import TextCompressor
from core.files import FilesCompressor
import os.path
import sys

def check_file(path):
	''' Make sure that the file exists '''
	if not os.path.exists(path):
		raise ValueError('The path specified does not exists.')

def choose_engine(path):
	''' Choose a compression engine according to the file type '''
	ext = path.split('.')
	if ext[-1] == 'ozip':
		ext = ext[-2]
	else:
		ext = ext[-1]
	if ext == 'txt':
		return TextCompressor()
	return FilesCompressor()

def main(path, decompress):
	''' Main function '''
	# Make sure the path is valid
	try:
		check_file(path)
	except ValueError, e:
		print str(e)
		sys.exit(1)
	# Get a compression engine usable with the input file
	engine = choose_engine(path)
	# Do the thing
	if decompress:
		try:
			engine.decompress(path)
			print 'Decompression done.'
		except Exception, e:
			print 'Something went wrong. Please issue a bug report on https://github.com/OzTamir/oZip/issues' + \
				' with a screenshot of this error.'
			print 'Error:\n%s' % str(e)
			return
	else:
		try:
			engine.compress(path)
			print '\n'.join(['Compression done.', \
							'Original file size: %s kb' % str(os.path.getsize(path) / 1024), \
							'Compressed file size: %s kb' % str(os.path.getsize(path + '.ozip') / 1024)])
		except Exception, e:
			print 'Something went wrong. Please issue a bug report on https://github.com/OzTamir/oZip/issues' + \
				' with a screenshot of this error.'
			print 'Error:\n%s' % str(e)
			return
