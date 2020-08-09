# CSS

## Root Element

The root element represents the `<html>` tag of an HTML document and is accessible using the `:root` selector. `:root` can be useful for declaring global CSS variables:

```css
:root {
  --main-color: hotpink;
  --pane-padding: 5px 42px;
}
```

---

## The difference between `rem`, `px` and `em` units

- The **rem** unit is relative to font-size of the root element of the document.
- The **em** unit is relative to font-size of the parent of element.
- The CSS **px** can be roughly regarded as a size to be seen comfortably by the naked human eye, not too small so you’d have to squint. A pixel value will looks the same, no matter what the device.

---

## Advantages of using `rem` or `em` over `px`?

Both **em** and **rem** are flexible, scalable units of measurements which are translated by the browser into pixel values. Because of these units ability to scale, these makes them very useful for accessibility. 

---

## `vh` and `vw` units.
`vw` stands for **viewport width** and 1vw is 1% of the width of the viewport.

`vh` stands for **viewport height** and 1vh is 1% of the height of the viewport.


---

## Result of selectors `.container` and `[class~=container]`?

The result is the same; both selections will return all elements with class `container`

---

## Result of selector `[class*=container]`?

The selector will return all elements with class that contains the keyword `container`.

---

## Repaint and Reflow?

Repaint occurs when visible changes are made to the element but does not affect it's layout. Reflow means re-calculating the positions and geometries of elements in the document, for the purpose of re-rendering part or all of the document.

A good example is `visibility: hidden` and `display: none`. The former does not cause a re-flow of the document but the latter does.

---
## `box-sizing` property.

`box-sizing` is used to calculated the height and width of an element.
- `content-box`: default value; the width and height only includes the content and not the border or padding.
- `border-box`: width and height properties includes border, padding and content.