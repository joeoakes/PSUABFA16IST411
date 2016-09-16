# import queue libary queue for python 3
import queue
# import only threading from Thread module
from threading import Thread

# Funtion that performs work
# Passes in queue object as q
# Gets the next item on the queue and prints it
# Tells the queue that processing the task is complete
def workerT(q):
  while True:
    print(q.get())
    q.task_done()

# setup the queue object as q 0 = infinite
# set the number of threads object to be 10
q = queue.Queue(maxsize=0)
num_threads = 10

# Loop to put 100 numbers on the queue
for x in range(100):
  q.put(x)

# looping 10 threads
# create a worker thread object
# worker is terminated when the main thread ends
# start the thread
for i in range(num_threads):
  worker = Thread(target=workerT, args=(q,))
  worker.setDaemon(True)
  print("Thread: "+ str(i))
  worker.start()

# wait unit the thread terminates
q.join()
