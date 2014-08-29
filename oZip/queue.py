# System modules
from Queue import Queue
from threading import Thread
import time
# oZip Handler
from main import main

def Worker(i, q, err_q, decompress):
	''' A Worker thread to process a file '''
	while True:
		# Get the next file from the queue
		filename = q.get()
		# Run the compression on the file
		res = main(filename, decompress)
		# If the return value is a tuple, than there were errors
		if isinstance(res, tuple):
			# Report the error using the error queue
			err_q.put(res)
		# Report that the worker is ready for another file
		q.task_done()

def runPool(f_list, err_q, should_compress=False, pool_size=5):
	''' Create a thread pool to process a queue of files '''
	# Don't create unemployed workers
	if len(f_list) < pool_size:
		pool_size = len(f_list)
	# Initialize a queue with the file names
	files_queue = Queue()
	# Set up the threads pool
	for i in range(pool_size):
		# Start the workers
	    worker = Thread(target=Worker, args=(i, files_queue, err_q, should_compress))
	    worker.setDaemon(True)
	    worker.start()

	# Add the files to the queue, from which the workers will pull new files
	for filename in f_list:
		files_queue.put(filename)
	        
	# Now wait for the queue to be empty (all files processed)
	files_queue.join()
	# Wait 'till all errors were reported
	err_q.join()
	# Add a message to signal that there aren't any other files waiting to be processed
	err_q.put('Done')
	return



