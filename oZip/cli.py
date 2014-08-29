from oZip.main import main as run
import argparse

def main():
	parser = argparse.ArgumentParser()

	parser.add_argument('-i', action='store', dest='path',
						help='Path to input file')

	parser.add_argument('-d', action='store_true', default=False,
						dest='should_decompress',
						help='Decompress a file')

	parser.add_argument('--version', action='version', version='oZip 1.0')

	results = parser.parse_args()
	path = results.path
	action = results.should_decompress
	run(path, action)

if __name__ == '__main__':
	main()