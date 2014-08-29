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
	# If the extansion is ozip, get the original format
	if ext[-1] == 'ozip':
		ext = ext[-2]
	# Get the file's format
	else:
		ext = ext[-1]
	# If it's a text file, use the text engine
	if ext == 'txt':
		return TextCompressor()
	# Else, use the filse engine
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
			# Try to decompress the file
			engine.decompress(path)
		except Exception, e:
			# Report if there were errors
			return (path, str(e))
	else:
		try:
			# Try to compress the file
			engine.compress(path)
		except Exception, e:
			# Report if there were errors
			return (path, str(e))
	return None









