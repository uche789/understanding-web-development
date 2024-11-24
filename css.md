# CSS

## Root Element

The root element represents the `<html>` tag of an HTML document and is accessible using the `:root` selector. `:root` can be useful for declaring global CSS variables:

```css
:root {
  --main-color: hotpink;
  --pane-padding: 5px 42px;
}
```


## The difference between `rem`, `px` and `em` units

The **rem** unit (also known as root em) is relative to `font-size` of the root element of the document. This mean that the root `font-size` of `16px` translates to `1rem`. 

The **em** unit is relative to `font-size` of the nearest parent of element.

**px** (pixels) can be roughly regarded as a size to be seen comfortably by the naked human eye, not too small so you’d have to squint. A pixel value will look the same, no matter what the device.


## Advantages of using `rem` or `em` over `px`?

Both **em** and **rem** are flexible, scalable units of measurements which are translated by the browser into pixel values. Because of these units' flexibility and scalability, they are very useful for accessibility and responsive design.

[Read more](https://blog.logrocket.com/using-em-vs-rem-css/#:~:text=em%20is%20a%20CSS%20unit,relative%20to%20a%20set%20value.) on the different units.


## `vh` and `vw` units.
`vw` stands for **viewport width** and 1vw is 1% of the width of the viewport.

`vh` stands for **viewport height** and 1vh is 1% of the height of the viewport.



## Result of selectors `.container` and `[class~=container]`?

The result is the same; both selections will return all elements with class `container`


## Result of selector `[class*=container]`?

The selector will return all elements with class that contains the keyword `container`.

## Repaint and Reflow?

Repaint occurs when visible changes are made to the element but does not affect its layout. Reflow means re-calculating the positions and geometries of elements in the document, for the purpose of re-rendering part or all of the document.

A good example is `visibility: hidden` and `display: none`. The former does not cause a re-flow of the document but the latter does.

## `box-sizing` property.

`box-sizing` is used to calculated the height and width of an element.
- `content-box`: default value; the width and height only includes the content and not the border or padding.
- `border-box`: width and height properties includes border, padding and content.

## What is specificity?

Specificity is the browser algorithms to determine which styles are the most relevant to an element and which css properties should be applied. Specificity is calculated based on a hierarchy of selectors. This is the order of CSS specificity hierarchy from lowest to highest:

1. Universal Selector (*)
2. Element/Type Selector (div, p, h1)
3. Class Selector, Attribute Selector, and Pseudo-Class
4. ID Selector
5. Inline Styles
6. Important Rules: Adding **`!important`** to a CSS declaration overrides any other rule, regardless of specificity.

## Psuedo class
CSS psuedo classes are keywords denoting special states or conditions of an element. For example, you might want to style a button if its is disabled or high a text if you hover over it.

Below are examples of psuedo classes:

1. `::after`, `::before`
2. `:disabled`, `:focus`, `:hover`
3. `:first-child()`, `:last-child()`, `:last-of-type()`, `:nth-child(n)`
4. `:has()`

