# Computing

## What is a thread?
Let’s take a train and a train track as a simple example. A train can only run on one track at a time. If you have more tracks, more trains can run at the same time. Similarly, a thread is just a path that helps a job move smoothly in a computer, one step at a time!

Threads is an execution context, which is the smallest set or sequence of instructions that a computer can manage. Threads share the same memory and resource with the same process, allowing for easier communication and data sharing.

A thread should not be confused for a process, which is a program executed by a computer system. A process can have one or more threads executing instructions concurently and enabling multitasking within a single application (see the section on multithreading) and typically has its own resources and memory.

```python
import threading
from threading import Thread

def task(num: int):
   print('Task is running: ' + str(num))


def single_thread():
   t = threading.Thread(target=task, args=(1,))
   t.start()

def main():
   single_thread()

main()
```

## What is a thread pool?
A railway company has a collection of trains and train tracks. A railway company will usually have more trains than tracks, so the trains need to run on a schedule. When a train is ready, it goes on an available track and once it reaches the end of its journey, it’s removed from the track and the track is then free for the next train. Instead of building new tracks, the company is reusing its tracks. Similarly, a thread pool manages pre-initialized threads, reusing them for multiple tasks.

A proper definition of a thread pool is a collection of worker threads that efficiently execute asynchronous callbacks on behalf of the application. Thread pools reduce the number of frequent thread creation and destruction and thus, improving the performance of an application that needs to handle many tasks concurrently.

```python
import threading
from threading import Thread

def task(num: int):
   print('Task is running: ' + str(num))

def multithreading():
   threads: list[Thread] = []
   for i in range(10):
       thread = threading.Thread(target=task, args=(i,))
       thread.start()
       threads.append(thread)
   for thread in threads:
       thread.join()
   print("All threads have finished.")

def main():
   multithreading()

main()
```

## What is multithreading?
Multithreading is a technique where multiple threads (smaller units of a process) run concurrently within a single process. Each thread shares the same memory space but can run independently. In short, the goal of multithreading is to run two things "alongside each other".

Multithreading is different from thread pools, as the threads are managed explicitly by the programmer. A thread pool automatically handles the thread management, reusing threads to reduce the cost of frequent thread creation and destruction. 

```python
import threading
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

def task(num: int):
   print('Task is running: ' + str(num))

def threadpool():
   with ThreadPoolExecutor(max_workers=3) as executor:
       for i in range(10):
           executor.submit(task, i)

def main():
   threadpool()

main()
```