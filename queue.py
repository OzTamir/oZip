# System modules
from Queue import Queue
from threading import Thread
import time
# oZip Handler
from oZip.main import main

def Worker(i, q):
	''' A Worker thread to process a file '''
	while True:
		filename = q.get()
		main(filename, False)
		q.task_done()

def runPool(f_list, should_compress=False, pool_size=3):
	''' Create a thread pool to process a queue of files '''
	# Don't create unemployed workers
	if len(f_list) < pool_size:
		pool_size = len(f_list)
	files_queue = Queue()
	# Set up the threads pool
	for i in range(pool_size):
	    worker = Thread(target=Worker, args=(i, files_queue,))
	    worker.setDaemon(True)
	    worker.start()

	# Download the feed(s) and put the enclosure URLs into
	# the queue.
	for filename in f_list:
		files_queue.put(filename)
	        
	# Now wait for the queue to be empty (all files processed)
	files_queue.join()
	return



