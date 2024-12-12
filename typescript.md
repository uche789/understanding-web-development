# Typescript

## Benefit of using Typescript over Javascript

Typescript is a superset of Javascript, meaning all the features of ECMAScript are available in Typescript. Typescript allows type-checking, which will reduce the risk of errors in larger projects.

## Access modifiers `public`, `private`, `protected`, and `readonly`

* `public` - the property or method is only accessible internally or externally
* `private` - the property or method is only accessible internally
* `protected` - the property and method is accessed within the class and or any class that extends it 
* `readonly` - the property cannot be reassigned after initialization. Typescript will throw a console error

## `abstract` keyword

The `abstract` keyword allows you to define a class with properties, methods and accessors with no implementation.

```Typescript
abstract class User {
  abstract doWork(): void;
}
```

## `static` keyword do

`static` Properties/methods are accessible without. `static` keyword are best used for utility methods.

This allows you

```Typescript
class Helper {

  key: string = '';

  constructor(keyValue) {
    this.key = keyValue;
  }

  static formatConfig() {
    //
  }  
}


Helper.formatConfig();
```

Note that you cannot access non-static properties and methods within a static method.

```Typescript
Helper.key //throws an error
```

## Usuage of `?` in the definition of a property in the interface?

`?` is used to mark the property as optional. 

```Typescript
interface Properties {
  id: string;
  name?: string;
}
```

## Symbols

Symbols are unique, immutable identifiers that can be used as object keys. 

```Typescript
const key = Symbol('id');
const anObject = {};
anObject[key] = 'aValue';
```

## Decorator

A decorator is a function that allows shorthand in-line modification of classes, properties, methods, and parameters. A method decorator receives 3 parameters:
* `target`: the object the method is defined on
* `key`: the name of the method
* `descriptor`: the object descriptor for the method

```Typescript
class AClass {
  
  @Decorator
  methodName() {
    //
  }
}
```