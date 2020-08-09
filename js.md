# Javascript

## `this`

The `this` keyword refers to the object it belongs to.
- In a function, `this` refers to the global object.
- In a method, `this` refers to the owner object.
- In a function, `this` refers to the global object.
- Methods like `call()` and `apply()` can refer this to any object.
- The `bind()` method has its `this` keyword set to the provided value.

---

## Difference between `map()` and `forEach()`

`map()` creates a new array with the results of the function called for every element in the given array. `forEach()` iterates over every element in a given array and does not return anything.

---

## Difference between `const`, `var` and `let` declarations

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

---
## Hoisting

Variable declarations are moved to the top of the current scope.

```javascript
x = 5;
var x;
```

---

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
---

## Promise

A `promise` object is the eventual completion resulting in success or failure of an asynchronous operation.

```javascript
new Promise(function(resolve, reject) {
  // do something
})
```

---

## Handling multiple Promises?

The `Promise.all` function will return a single promise that fulfills once all the promises passed as iterable have been fulfilled.

```javascript
const promise1 = Promise.resolve(40);
const promise2 = new Promise();
const results = Promise.all([promise1, promise2]).then(function (values) => {
  // do something here
});
```

---

## `async`/`await`?

`async`/`await` was introduced in ES7 to simplify promises and keep code readable. An `await` expression pauses the execution of the async function until the promise has been resolved. 

```javascript
async function anAsyncFunc() {
  return await methodCallAsync();
}

async function aMethod() {
  const result = await anAsyncFunc();
  console.log(result.value);
}
```

---

## Immutable and mutable object

An immuntable object is a object whose state cannot be modified after it has been created. Strings and numbers are immutable. Functions, arrays, classes and objects are mutable.

Immutability should not be confused with variables declared using the `const` keyword. The reference of the constant is immutable however, this does not mean that the value is immutable. Take the object below as an example:

```javascript
const anObject = {
  prop: ''
}
```

`anObject` cannot be redeclared or reassigned, however, we can change the value of `prop`.