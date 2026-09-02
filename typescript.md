# TypeScript

- [Benefit of using TypeScript](#benefit-of-using-typescript)
- [`interface` and `type`](#`interface`-and-`type`)
- [enums or Object.freeze(object)](#enums-or-object.freeze(object))
- [Access modifiers `public`, `private`, `protected`, and `readonly`](#access-modifiers-`public`,-`private`,-`protected`,-and-`readonly`)
- [`abstract` keyword](#`abstract`-keyword)
- [Difference between using an abstract class over an interface](#difference-between-using-an-abstract-class-over-an-interface)
- [`static` keyword do](#`static`-keyword-do)
- [Optional parameters using `?`](#optional-parameters-using-``)
- [Symbols](#symbols)
- [Decorator](#decorator)
- [Why TypeScript an unsound language](#why-typescript-an-unsound-language)
  - [Further reading](#further-reading)
- [Generics](#generics)
- [Overloaded functions](#overloaded-functions)

## Benefit of using TypeScript

TypeScript is a superset of Javascript, meaning all the features of ECMAScript are available in TypeScript. TypeScript allows type-checking, which will reduce the risk of errors in larger projects.

The [TypeScript handbook](https://www.typescriptlang.org/docs/handbook/intro.html) provides comprehensive explanations about TypeScript.

## `interface` and `type`

interface and type

`type` allows more flexibility

## enums or Object.freeze(object)

the different types

## Access modifiers `public`, `private`, `protected`, and `readonly`

* `public` - the property or method is only accessible internally or externally
* `private` - the property or method is only accessible internally
* `protected` - the property and method is accessed within the class and or any class that extends it 
* `readonly` - the property cannot be reassigned after initialization. TypeScript will throw a console error

## `abstract` keyword

The `abstract` keyword allows you to define a class with properties, methods and accessors with no implementation.

```TypeScript
abstract class User {
  abstract doWork(): void;
}
```

## Difference between using an abstract class over an interface

TBP

## `static` keyword do

`static` Properties/methods are accessible without. `static` keyword are best used for utility methods.

This allows you

```TypeScript
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

```TypeScript
Helper.key //throws an error
```

## Optional parameters using `?`

`?` is used to mark the property as optional. 

```TypeScript
interface Properties {
  id: string;
  name?: string;
}
```

## Symbols

Symbols are unique, immutable identifiers that can be used as object keys. 

```TypeScript
const key = Symbol('id');
const anObject = {};
anObject[key] = 'aValue';
```

## Decorator

A decorator is a function that allows shorthand in-line modification of classes, properties, methods, and parameters. A method decorator receives 3 parameters:
* `target`: the object the method is defined on
* `key`: the name of the method
* `descriptor`: the object descriptor for the method

```TypeScript
class AClass {
  
  @Decorator
  methodName() {
    //
  }
}
```

## Why TypeScript an unsound language

TypeScript is considered unsound because it allows type safety for certain operations that cannot be guaranteed at compile-time. For example, the `Event` type might be used to represent a MouseClick event, even though its exact runtime type cannot be strictly verified at compile-time.

```TypeScript
// this is unsound
function handleMouseClickEvent(event: Event) {
  // ...
}
```

### Further reading
- https://www.TypeScriptlang.org/docs/handbook/type-compatibility.html

## Generics

## Overloaded functions

TypeScript allows overloaded functions, whereby a function can be called with different paramaters. 

```TypeScript
function getUser(firstname: string|number, lastname: string): User|undefined;
function getUser(identifier: string|number): User|undefined;
function getUser(identifier: string|number, firstname?: string, lastname?: string): User|undefined {
  // do something
}
```