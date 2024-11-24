# HTML (HyperText Markup Langugage)

## Doctype declaration

The doctype declaration is an instruction to the web browser on what HTML version the page is written in. This ensures that the web page is parsed the same way in every browser. The most reliable doctype declaration for HTML5 is `<!DOCTYPE html>`.

## `async` and `defer` attributes in the `<script>` tag

`async` loads and executes the external Javascript file completely independently of the page. 
`defer` loads the external Javascript file but does not execute it until the page is loaded (the DOM is ready) and before `DOMContentLoaded` event is fired.

Both attributes improves page load speeds as the page is never blocked by the Javascript loading and execution.

## meta tag

The `<meta>` tag provides metadata about the HTML document. These include description, keywords and viewport information.

The `<meta>` viewport element should be included in all your web pages to support mobile devices.

```HTML
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## Difference between a `cookie`, `sessionStorage` and `localStorage`?

A `cookie` stores a small piece of data stored in the user's web browser and is used to store stafeful information. One common web cookie is the **authentication cookie** (also known as session cookie) which is used to remember if the user is logged in or not. Cookies are also used to remember users preferences such a themes and language, and also to analyze user behaviour.

`sessionStorage` property access a browser session object. The storage data is cleared once the page sessions has ended (the browser window or tab is closed).

`localStorage` property is similar to the sessionStorage except that it never expires.

*Data stored in either `localStorage` or `sessionStorage` is specific to the protocol of the page.*


## `data-` attribute?

`data-*` attributes allow us to store extra/custom information on HTML DOM elements that is not essential or visible to the user.


## `srcset` attribute

`srcset` attribute is used to specify image candidate strings and indicates the conditions (width or pixel density descriptor) under which the candidate should be used instead of the image specified by the `src` property. This is great for responsive design.



## Placement of CSS `<link>` tag and the Javascript `<script>` in the HTML document

The `<link>` tag should be placed in the header of the document. Javascript `<script>` without the `deferred` or `async` attribute should be placed at the bottom of the `body` tag as you want the DOM Elements to be ready before loading and executing any javascript.

## `rel="noopener"` or `rel="noreferer" attributes

`rel="noopener"` or `rel="noreferrer"` are added to links that use `target="_blank"` attribute so that the page being redirected does not run on the same process as the current page. This can improve performance if the page being opened is running a lot of Javascript. Using `rel="noopener"` will not allow the other page from accessing your window object with the window.opener property thus preventing an attack surface because the other page can potentially redirect your page to a malicious URL.

* rel="noopener" prevents the new page from being able to access the window.opener property and ensures it runs in a separate process.
* rel="noreferrer" attribute has the same effect, but also prevents the Referer header from being sent to the new page.

## Progressive rendering

Progressive rendering are techniques used to render display content as quickly as possible. Two examples are:

* **Lazy loading of images:** Images are loaded by Javascript only when they becoming visible in the viewport.
* **Prioritizing visible content:** sometimes referred to as "above the fold", only the minimum css/content/scripts necessary is included for the amount of page visible to the user. *Anything that isn't immediately visible to the user is considered "below the fold"*.

## Virtual DOM

The DOM is the object-based representation of the HTML document. The virtual DOM is an abstraction of the original DOM and is used to make frequent updates, which are later applied to the DOM in a more performant way.

## Shadow DOM

The Shadow DOM api provides a way attach a hidden separated DOM to an element to allow encapsulation of code (markup structure, style, and behavior) on a page so that different parts do not clash, and the code can be kept nice and clean. The code encapsulated inside the shadow DOM has no effect on anything outside it.

```html
<my-element></my-element>

<script>
    class MyElement extends HTMLElement {
        constructor() {
            super();

            // Create a shadow root
            const shadow = this.attachShadow({ mode: 'open' });

            const wrapper = document.createElement('div');
            wrapper.innerHTML = `<p style="color: red">This is a web component</p>`;

            shadow.appendChild(wrapper);
        }
    }

    // Register the custom element
    customElements.define('my-element', MyElement);    
</script>
```

The Shadow DOM can be used to create web components.

## What are a few ways to improve the performance of a web page?

- **Minify CSS, JavaScript, and HTML.**
- **Use a Content Delivery Network (CDN).**
- **Lazy-loading:** Lazy-load images only when they appear in the viewport. Lazy-loading components and Javascript libraries only when in use.
- Reduce requests sent to the server: if you're using a modern web-framework such as Vue or React, consider using TanStack Query or Vue query to handle data-fetching, caching, synchronization and mutations.
- **Compress images using image tools.** 
- **Use less animations.**
- **Enable browser caching:** you can configure your web application so that the browser will cache the files it receives from the server

## How can I improve the accessibility of a website?
- **Use Alt Text for Images:** Add descriptive alt attributes for all images. If the image is decorative and does not convey any meaning, the value of Alt should be empty.
- **Keyboard Navigation:** Ensure all interactive elements (links, buttons, forms) are accessible via keyboard.
- **Use ARIA Roles:** ARIA attributes help improve accessibility for assistive technologies. However, use semantic HTML instead ARIA attributes when possible.
- **Color Contrast:** Test color contrast ratios to ensure text is readable for people with visual impairments. WebAIM provides a [color contract checker](https://webaim.org/resources/contrastchecker/).
- **Use heading levels:** Use the correct hierachy for headings (h1-h6)

