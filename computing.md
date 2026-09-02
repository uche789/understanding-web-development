# Computing & Programming

- [What is a thread?](#what-is-a-thread)
- [What is a thread pool?](#what-is-a-thread-pool)
- [What is multithreading?](#what-is-multithreading)
- [SOLID principle](#solid-principle)
  - [Example of the Interface Segregation Principle](#example-of-the-interface-segregation-principle)
  - [Example of the Dependency Inversion Principle](#example-of-the-dependency-inversion-principle)
  - [Example of Liskov Substitution](#example-of-liskov-substitution)
- [Polymorphism and inheritance](#polymorphism-and-inheritance)
- [What is reactive programming?](#what-is-reactive-programming)
  - [Further reading(s)](#further-reading(s))
- [What is dynamic programming?](#what-is-dynamic-programming)
  - [Memoization (Top-Down)](#memoization-(top-down))
  - [Tabulation (Bottom-Up)](#tabulation-(bottom-up))
  - [Further readinsg(s)](#further-readinsg(s))
- [Soundness and Safety in Programming Languages](#soundness-and-safety-in-programming-languages)
- [Agile vs Scrum vs Waterfall vs Kanban](#agile-vs-scrum-vs-waterfall-vs-kanban)

## What is a thread?
Let’s take a train and a train track as a simple example. A train can only run on one track at a time. If you have more tracks, more trains can run at the same time. Similarly, a thread is just a path that helps a job move smoothly in a computer, one step at a time!

Threads is an execution context, which is the smallest set or sequence of instructions that a computer can manage. Threads share the same memory and resource with the same process, allowing for easier communication and data sharing.

A thread should not be confused for a process, which is a program executed by a computer system. A process can have one or more threads executing instructions concurrently and enabling multitasking within a single application (see the section on multithreading) and typically has its own resources and memory.

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

A proper definition of a thread pool is a collection of worker threads that efficiently execute asynchronous callbacks on behalf of the application. Thread pools reduce the number of frequent thread creation and destruction and thus, improves the performance of an application that handles many tasks concurrently.

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

## SOLID principle

SOLID stands for the five design principles:
- **Single responsiblility**
- **Open/Closed:** software entites should be open for extension, closed for modification (ex: visitor pattern)
- **Liskov substitution:** objects of a superclass by be substituted for objects of a subclass without breaking the application.
- **Interface segregation:** a class should not be forced to implement methods that it does not need.
- **Dependency inversion:** high-level modules should not depend on abstractions and not import anything from low-level modules.

### Example of the Interface Segregation Principle

```php
interface Customers {
    public function getAddress();
    public function getVipPoints();
}

class VIPCustomer {
    public function getAddress() {
        // ...
    }
    
    public function getVipPoints() {
        // ...
    }
}


interface BasicCustomer {
    public function getAddress() {
        // ...
    }

    // should not be forced to implement this
    public function getVipPoints() {
        // ...
    }
}
```

### Example of the Dependency Inversion Principle

```php

// High-level module
class User {
    
    public string $userEmail;

    // Dependency is injected via the constructor
    public function __construct(private IEmailService emailService) {
    }

    public function notifyUser() {
        $this->emailService->sendEmail($this->userEmail);
    }
}

interface IEmailService {
    public function sendEmail();
}

class EmailServiceImpl implements IEmailService {
    public function sendEmail(string $userEmail) {
        // send email
    }
}

// Set up the DI container
$container = new Container();

$container['EmailService'] = function () {
    return new EmailServiceImpl();
};

$container['User'] = function ($c) {
    return new User($c['EmailService']);
};

// Use the container to resolve dependencies
$userService = $container['UserService'];
$userService->notifyUser("test@example.com");
```

### Example of Liskov Substitution

https://stackoverflow.com/questions/56860/what-is-an-example-of-the-liskov-substitution-principle

## Polymorphism and inheritance

Inheritance is when a class inherits methods and properties from another class. Polymorphism is the act of using this methods to perform various tasks. Polymorphism means differents forms.

```php
class GeometricObject () {
    public function draw() {}
}

class Square extends GeometricObject {
    public function draw() {}
}

class Triangle extends GeometricObject {
    public function draw() {}
}


$square = new Square();
$triange = new Triangle();

// results of both draw() methods will not be the same
$square->draw();
$triange->draw();
```

## What is reactive programming?

Reactive programming is a declarative programming paradigm that focuses on data streams and propagation of changes. React programming relies on asynchronous logic to handle real-time changes to data, making it particular useful for applications that require dynamic and responsive behaviour.

Reactive programming is beneficial for modern use cases like dynamic UIs and real-time data processing.

### Further reading(s)
[Reactive Extensions Library for JavaScript](https://rxjs.dev/guide/overview)

## What is dynamic programming?
Dynamic programming is a method of breaking down problems into sub problems and storing the solution to optimize time and space complexity, typically using memoization or tabulation.

### Memoization (Top-Down)
Storing results of subproblems in a table to avoid recomputation. This is done recursively.

### Tabulation (Bottom-Up)
Building solutions iteratively from smaller subproblems to larger ones.

### Further readinsg(s)
- [Real-world Use Cases of Dynamic Programming](https://hackernoon.com/real-world-use-cases-of-dynamic-programming)
- [What is Dynamic Programming? Working, Algorithms, and Examples](https://www.spiceworks.com/tech/devops/articles/what-is-dynamic-programming/)

## Soundness and Safety in Programming Languages

Safety means that there is a guarantee that all operations will be performed on meaningful data. For example, a string cannot be added to a number while performing an additional, or we ensure that in division, the second argument cannot be zero.

In an untyped language, a piece of data is not associated with any data types. There are two types of typed languages:
- In **statically typed languages**, the programmer has to explicitly state the data type of a value. Examples of statically typed languages include Java, C# and C++.
- In **dynamically typed languages**, the data type can be assigned during run-time checks.  Examples of dynamically typed languages include JavaScript, Python, and Ruby.

A programming language is considered sound if a program passes static type checks at compile-time and guarantees the absence of type errors at runtime. Type soundness ensures that, for any given expression, its evaluated result will always conform to the static type assigned at compile-time.

Examples of sound languages include Dart, C#, and Java. On the other hand, unsound languages such as TypeScript, JavaScript, Python, and C do not provide such guarantees, which can lead to type errors during runtime despite passing compile-time checks.

The benefits of soundness include improved code readability, maintainability, and the early detection of type errors at compile-time, reducing potential bugs in production.

In general, type-safety and type soundness are the extent to which a programming language will prevent type errors.

- https://dart.dev/language/type-system
- https://papl.cs.brown.edu/2015/safety-soundness.html

## Agile vs Scrum vs Waterfall vs Kanban

TBP
