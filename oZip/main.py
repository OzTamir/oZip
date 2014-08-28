from core.text import TextCompressor
from core.files import FilesCompressor
import os.path
import sys

def check_file(path):
	if not os.path.exists(path):
		raise ValueError('The path specified does not exists.')

def choose_engine(path):
	ext = os.path.splitext(path)
	if ext == '.txt':
		return TextCompressor()
	return FilesCompressor()

def main(path, decompress):
	try:
		check_file(path)
	except ValueError, e:
		print str(e)
		sys.exit(1)

	engine = choose_engine(path)
	if decompress:
		engine.decompress(path)
	else:
		engine.compress(path)

	print 'Thanks for using oZip'
	sys.exit(0)
