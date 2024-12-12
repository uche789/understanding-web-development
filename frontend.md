# Frontend

This page covers general frontend-specific topics. The following pages also fall under frontend:

- [CSS](css.md)
- [HTML](html.md)
- [Typescript](typescript.md)
- [Javascript](javascript.md)

For system design topics, refer to the [System Design](system-design.md) page.

## What is a circular dependency and how can it be avoided?

Circular dependencies occur when two or more modules (or components) reference each other, creating a loop. This can be avoided by decoupling shared code into its own module.

Circular dependencies can be avoided by:
- **Decoupling the code.** This means organizing the code into smaller, independent modules that don’t rely on each other in a circular fashion.
- **Shared logic should be in a separate module**, which can then be used by other modules without causing circular references.

## What are memory leaks happen in Javascipt and how can it be avoided?

A memory leak occurs when memory that is no longer needed is not released, causing the global space to fill up with unreachable variables and functions that cannot be collected by the garbage collector.

Memory leaks can be avoided by:
- Defining variables within a closed scope ensures they are properly cleaned up when no longer needed.
- Avoiding global variables that remain in memory unnecessarily.
- Properly cleaning up event listeners, intervals, and timeouts that hold references to objects after they're no longer needed.
- Weak references or WeakMaps can also help, especially when objects are no longer needed but still referenced.

