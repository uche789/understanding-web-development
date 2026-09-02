# Javascript

## What does the `this` keyword refer to?

The `this` keyword refers to the object it belongs to.
- In a function, `this` refers to the global object.
- In a method, `this` refers to the owner object.
- In a function, `this` refers to the global object.
- Methods like `call()` and `apply()` can refer this to any object.
- The `bind()` method has its `this` keyword set to the provided value.

## What is the difference between `map()` and `forEach()`?

`map()` creates a new array with the results of the function called for every element in the given array. `forEach()` iterates over every element in a given array and does not return anything.

## What does the array propery `reduce` do?

`reduce()` executes a **reducer** callback on each value in an array and returns an accumulated value as the result. This is useful for operations related to aggregation and summation of data.

### Example

```javascript
const initialValue = 0;
const sum = [1, 4, 6, 7].reduce((accumulator, currentValue) => prev + cur, initialValue); // value = 18
```

## What is the difference between `const`, `var` and `let` variable declarations?

* `const` - the variable cannot be redefined and cannot be changed through reassigment

```javascript
const aString = 'This is a string';
aString = 'This is the modified string';

// console error:
// Uncaught TypeError: Assignment to constant variable.

const anObject = { aProp: 'aValue' };

console.log(anObject.aProp); // prints aValue

anObject.aProp = 'aNewValue';

console.log(anObject.aProp); // prints aNewValue
```

* `var` - the variable will be processed first before any code is executed, irrespective of where it was declared (see hoisting)

* `let` - the variable not be redeclared and are block-scoped but they can be reassigned;

```javascript
let aString = 'This is a string';
console.log(aString); // 'This is a string'
aString = 'This is the modified string';
console.log(aString); // This is the modified string
```

*Declared variables are constrained in the execution context (scope) in which they are declared.*

```javascript
function x() {
  const a = 'aVariable';
  let b = 'bVariable';
  var c = 'cVariable';
}

//Throws a ReferenceError
console.log(x(a));
console.log(x(b));
console.log(x(c));
```

## Hoisting

Hoisting is what happens when variable declarations are moved to the top of the current scope.

```javascript
function run () {
  function addTen() {
    return x + 10;
  }
  var x = 5;
}
```
The variable `x` will be hoisted to the top of the `run` function.


## AJAX request

AJAX (*Asynchronous JavaScript + XML*) is used to create ascyhronous web applications. Browsers have the `XMLHttpRequest` object which is used to make requests to a webserver. This allows you to update certains portions of a page without a full page reload.

```javascript
var xhr = new XMLHttpRequest();
xhr.open('GET', 'http://anUrl');
xhr.send();
xhr.onreadystatechange = function () {
  if (xhr.readyState == XMLHttpRequest.DONE) {
    // do something
  }
}
```

## Promise

A `promise` object is the eventual completion resulting in success or failure of an asynchronous operation.

```javascript
new Promise(function(resolve, reject) {
  // do something
})
```

## Handling multiple Promises

When running async operations concurrently, using the [`Promise.all`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all) will execute all async operations independently to significantly reduce execution time. It will return a single promise that fulfills once all the promises passed as iterable have been fulfilled.

```javascript
const promise1 = Promise.resolve(40);
const promise2 = new Promise();
const results = Promise.all([promise1, promise2]).then(function (values) => {
  // do something here
});
```

## `async`/`await`

`async`/`await` was introduced in ES7 to simplify promises and keep code readable. The `async` keyword indicates that a function will perform asynchronous operations, while the `await` keyword pauses the execution of the async function until the promise it’s waiting for is resolved.

```javascript
async function anAsyncFunc() {
  return await methodCallAsync();
}

async function aMethod() {
  const result = await anAsyncFunc();
  console.log(result.value);
}
```

`async`/`async` eliminates the need for promise chaining and nested callbacks.


## Immutable and mutable object

An immuntable object is a object whose state cannot be modified after it has been created. Strings and numbers are immutable. Functions, arrays, classes and objects are mutable.

Immutability should not be confused with variables declared using the `const` keyword. The reference of the constant is immutable however, this does not mean that the value is immutable. Take the object below as an example:

```javascript
const anObject = {
  prop: ''
}
```

`anObject` cannot be redeclared or reassigned, however, we can change the value of `prop`. When an object is created, memory is allocated for it, and the variable `anObject` stores a reference to that object in memory.

JavaScript automatically handles memory allocation and deallocation through garbage collection, which removes objects that are no longer referenced.

### Further Reading

- [Functional Programming in JS, part II - Immutability (Vanilla JS, Immutable.js and Immer)]https://dev.to/mpodlasin/functional-programming-in-js-part-ii-immutability-vanilla-js-immutable-js-and-immer-2ccm

## What is the V8 engine?
The V8 engine is built using C++ to execute JavaScript on a machine. It converts JavaScript into machine code using techniques like JIT compilation, which optimizes the execution of JavaScript for better performance.

The V8 engine powers Google Chrome and Node.js, making it a critical component for web browsers and server-side JavaScript execution.

## Hashmaps in Javascript

A hashmap (also known as a an associative array or an object), is a key-value data structure. In Javascript, a hashmap can be created using an object literal `{}`.

For example:

```javascript
let map = {};

map['key1'] = 'value 1';
map['key2'] = 'value 2';

// delete a key-value pair
delete map['key1']
```

The `Map` object can also be used.

```javascript
cosnt map = new Map();


map.set('key1', 'value1');
map.set('key2', 'value2');

if (map.has('key2')) {
  // delete a key-value pair
  map.delete('key1')
}
```

Javascript handles **key collisions** (two or more keys have the same hash value) implictly. This means that setting a new value for an existing key will override the old value. 

## What is the difference between a weak and strong reference?

A weak reference is a reference to an object that does not prevent the object from being garbage-collected, making it a crucial concept in memory management. `WeakSet` and `WeakMap` were introduced in the ES6 specification to leverage this concept for efficient memory handling and better management of object references.

Example of creating a weak reference using WeakMap:

```javascript
const weakMap = new WeakMap();

let person = {name: 'Jane Smith'};

weakMap.set(person, true)

console.log(weakMap) // prints WeakMap {{…} => true}

person = null;

console.log(weakMap)
```

When Javascript runs the garbage collector, the `obj` object will be removed, as well as the weak reference.

On the contrary, a strong reference prevents an objected from being collected by the garbage collector

Example of creating a strong reference:

```javascript
let person = {name: 'Jane Smith'}
let persons = [person]
person = null
console.log(persons) // prints [{name: 'Jane Smith'}]
console.log(person) // returns null
```

The object cannot be accessed via the `person` variable but is accessible in the `persons` array. 

## Event Loop

Event loops manages the execution of code, and enables asynchronous programming in Javascript while being single-threaded.

The event loop has the following components:

* **Call stack:** 
* **Background / Web APIs:** These handles async operations, such as browser features (e.g, `setTimeout`), DOM events, and HTTP requets. 
* **Microtask queue:** A high-priority queue for promises and 
* **Callback queue:**

### How it works?

1. It checks call stack to see if it's empty.
2. If the call stack is empty, it checks the Microtask Queue and pushes tasks from the queue to the call stack until all the tasks are executed. 
3. If there are no tasks in the Microtask Queue, it checks the Callback Queue and pushes the oldest task from the queue to the call stack.

### Further readings
- [The JavaScript Event Loop Explained with Examples](https://medium.com/@ignatovich.dm/the-javascript-event-loop-explained-with-examples-d8f7ddf0861d)
- [JavaScript execution model](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model#job_queue_and_event_loop)
- [Tasks vs. microtasks](https://developer.mozilla.org/en-US/docs/Web/API/HTML_DOM_API/Microtask_guide#tasks_vs._microtasks)

## Scoping

## Prototypal Inheritance

Prototypal Inheritances is when a child object inherits the properties and methods of its parent.

## Closures

Closure gives a block of code access to its outer scope, also known as **lexical environment**.

Examples:

```javascript
function sum(nums, even = false) {
  function getOnlyEven() {
    return nums.filter(num => num % 2 === 0);
  }

  return (even ? getOnlyEven() : nums).reduce((sum, curr) => sum + curr, 0);
}
```

## Modules


### Further reading

## Memory management

## Resource management
