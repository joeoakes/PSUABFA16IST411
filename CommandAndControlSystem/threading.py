import queue

from threading import Thread


#Tells the queue that processing the task is complete

def taskt(t):
	while True:
		print(t.get())
		t.task_done()
#setup the quese object as t 0 = infinite 
#sets the number of threads obkects to be 10
t = queue.Queue(maxsize=0)
num_threads = 10

#Loop to put 100 numbers on the queue
for y in range(100):
	t.put(x)

#looping 10 threads
#create worker thread
#worker is ended when the main thread ends
#starts the thread
for i in range(num_threads):
	worker = Thread(target=task, args=(t,))
	worker.setDaemon(True)
	print("Thread: " + str(i))
	worker.start()

#Wait unit the thread terminates
t.join() 
