# HTML

## Doctype declaration

The doctype declaration is an instruction to the web browser on what HTML version the page is written in. This ensures that the web page is parsed the same way in every browser. The most reliable doctype declaration for HTML5 is `<!DOCTYPE html>`.

---
## `async` and `defer` attributes in the `<script>` tag

`async` loads and executes the external Javascript file completely independently of the page. 
`defer` loads the external Javascript file but does not execute it until the page is loaded (the DOM is ready), but before `DOMContentLoaded` event.

Both attributes improves page load speeds as the page is never blocked by the Javascript loading and execution.
___
## meta tag

The `<meta>` tag provides metadata about the HTML document. These include description, keywords and viewport information.

The `<meta>` viewport element should be included in all your web pages to support mobile devices.

```HTML
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

___

## Difference between a `cookie`, `sessionStorage` and `localStorage`?

A `cookie` stores a small piece of data stored in the user's web browser and is used to store stafeful information. One common web cookie is the **authentication cookie** which is used to remember if the user is logged in or not. Cookies are also used to remember users preferences such a themes and language, and also to analyze user behaviour.

`sessionStorage` property access a browser session object. The storage data is cleared once the page sessions has ended (the browser window or tab is closed).

`localStorage` property is similar to the sessionStorage except that it never expires.

*Data stored in either `localStorage` or `sessionStorage` is specific to the protocol of the page.*

___

## `data-` attribute?

`data-*` attributes allow us to store extra/custom information on HTML DOM elements that is not essential or visible to the user.

___

## `srcset` attribute

`srcset` attribute is used to specify image candidate strings and indicates the conditions (width or pixel density descriptor) under which the candidate should be used instead of the image specified by the `src` property. This is great for responsive design.

___

## Placement of CSS `<link>` tag and the Javascript `<script>` in the HTML document

The `<link>` tag should be placed in the header of the document. Javascript `<script>` without the `deferred` or `async` attribute should be placed at the bottom of the `body` tag as you want the DOM Elements to be ready before loading and executing any javascript.

---
## `rel="noopener"` or `rel="noreferer" attributes

`rel="noopener"` or `rel="noreferrer"` are added to links that use `target="_blank"` attribute so that the page being redirected does not run on the same process as the current page. This can improve performance if the page being opened is running a lot of Javascript. Using `rel="noopener"` will not allow the other page from accessing your window object with the window.opener property thus preventing an attack surface because the other page can potentially redirect your page to a malicious URL.

* rel="noopener" prevents the new page from being able to access the window.opener property and ensures it runs in a separate process.
* rel="noreferrer" attribute has the same effect, but also prevents the Referer header from being sent to the new page.
___
## Progressive rendering

Progressive rendering are techniques used to render display content as quickly as possible. Two examples are:

* **Lazy loading** of images. Images are loaded by Javascript only when they becoming visible in the viewport.
* **Prioritizing visible content** (sometimes referred to as "above the fold") where you include only the minimum css/content/scripts necessary for the amount of page visible to the user.

___
## Virtual DOM

The DOM is the object-based representation of the HTML document. The virtual DOM is an abstraction of the original DOM and is used to make frequent updates, which are later applied to the DOM in a more performant way.

---
## Shadow DOM

The Shadow DOM api provides a way attach a hidden separated DOM to an element to allow encapsulation of code (markup structure, style, and behavior) on a page so that different parts do not clash, and the code can be kept nice and clean. None of the code inside a shadow DOM can affect anything outside it.

---
## JWT and JWS.

JWT (JSON Web Token) is a standard to generate access tokens from credentials which a user uses to access a resource. JWS (JSON Web Signature) is a standard for signing arbitrary and is used as the basis for other web-based technologies such as JWT.