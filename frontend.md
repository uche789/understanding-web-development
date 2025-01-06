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


## What are source maps?

Source maps are supplementary JavaScript files that assist with debugging in production. To improve performance, it is common practice to minify assets. However, minification makes the code difficult to read and debug. Source maps make debugging easier and can be enabled using most frontend build tools. Source maps can be a double-edged sword because they expose your source code to the public, potentially revealing proprietary information or security vulnerabilities.

### References

https://web.dev/articles/source-maps

## Immutability

https://dev.to/mpodlasin/functional-programming-in-js-part-ii-immutability-vanilla-js-immutable-js-and-immer-2ccm

## What are a few ways to improve the performance of a web page?

- **Minify CSS, JavaScript, and HTML.**
- **Use a Content Delivery Network (CDN).**
- **Lazy-loading:** Lazy-load images only when they appear in the viewport. Lazy-loading components and Javascript libraries only when in use. Lazy-load content using the Javascript native `IntersectionObserver` API or a library like `lazysizes`.
- Reduce requests sent to the server: if you're using a modern web-framework such as Vue or React, consider using TanStack Query or Vue query to handle data-fetching, caching, synchronization and mutations.
- **Compress images using image tools.** 
- **Use less animations:** Profilers such as Web Vitals and Lighthouse provide in-depth reports that can help you identify performance issues related to animations.
- **Enable browser caching:** you can configure your web application so that the browser will cache the files it receives from the server
- **Use browser Network Tabs:** Check if API requests are excessive and responses are large or slow. Check cache headers (e.g., ETag, Cache-Control) for proper caching strategies.
- **Conduct an audit of your assets:** Check the size and number of assets using tools like a bundle analyzer (bundle size) and network tab in DevTools to examine asset load times and sizes. Optimize with techniques such as tree-shaking, code splitting, and minification.
- **Use tools:** Chrome devTools (Performance insights tools, Web Vitals, Lighthouse Network tabes) can audit the performance of the webpage such as reflow and repaint issues.
- **Use Google PageSpeed Insights:** [PageSpeed Insights](https://pagespeed.web.dev/) analyzes your website's performance and provides actionable recommendations to improve speed and user experience. It evaluates both mobile and desktop performance and assigns a score based on metrics like load time, interactivity, and visual stability.
- **Remove unused CSS:** Unused CSS file size decreases your web performance or Speed. (Read more [here](https://medium.com/frontendweb/how-to-find-unused-css-in-the-website-54d773d76b65)).

## What is the difference between tree-shaking and code splitting?

Tree-shaking removes unused code from your bundle. Most modern bundlers (e.g., Vite, Rollup, Webpack) have tree-shaking configuration. Tree-shaking can also be achived by using ES modules (import/export) instead of CommonJS (require) for better tree-shaking compatibility and avoid using wildcard imports (e.g., import * as library), as they may include unnecessary modules.

Code splitting splits codes into smaller chunks that can be loaded on demand. This can be acheived using [dynamic imports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import) for lazy loading and configuration in bundlers such as Vite's `build.rollupOptions.output.manualChunks` and Webpacks `SplitChunksPlugin`.

## What is lazy-loading?

Lazy-loading is an approach that loads content only when it becomes visible in the user's viewport, improving page load times and performance.

## How can I improve the accessibility of a website?
- **Use Alt Text for Images:** Add descriptive alt attributes for all images. If the image is decorative and does not convey any meaning, the value of Alt should be empty.
- **Keyboard Navigation:** Ensure all interactive elements (links, buttons, forms) are accessible via keyboard.
- **Use ARIA Roles:** ARIA attributes help improve accessibility for assistive technologies. However, use semantic HTML instead ARIA attributes when possible.
- **Color Contrast:** Test color contrast ratios to ensure text is readable for people with visual impairments. WebAIM provides a [color contract checker](https://webaim.org/resources/contrastchecker/).
- **Use heading levels:** Use the correct hierachy for headings (h1-h6)
- **Use assistive tools:** Use screen readers such as VoiceOver, ChromeVox, and NonVisual Desktop Access (NVDA) to understand how users with disabilities interact with your application. Additionally, use tools like [Axe devetools linter](https://www.deque.com/axe/devtools/linter/) to identify and fix accessibility issues in your codebase. Tools like Google Lighthouse can also audit your website’s accessibility, performance, and best practices, providing actionable insights to improve user experience.

## How can you improve rendering performance in React?
 
- Cache expensive calculations using `useMemo` and memoize functions with `useCallback` to maintain stable references (unless the dependencies change), preventing unnecessary recalculations and re-rendering.
- Wrap functional components with `React.memo` to prevent re-renders if props haven’t changed.
- Use `React.lazy` and `Suspense` to load components only when needed.
- Use libraries like [React Window](https://github.com/bvaughn/react-window) or [React Virtualized](https://github.com/bvaughn/react-virtualized) to render only the visible items in a list.
- Avoid Inline functions or objects, which can create new references on every render, triggering re-renders (e.g., `<button onClick={() => console.log('click')}>Click me</button>`).
- Use a debounce function (e.g., with lodash) for expensive operations like search or scroll events. (e.g., `const search = useCallback(debounce(()=> {search(query)}, 280), [query])`).
- Use className over inline styles, as inline styles can trigger recalculations.

## How can you improve rendering performance in Vue?

- Use `computed` properties for expensive calculations.
- Use the v-once directive to render static content only once.
- Use `watch` and `watchEffect` sparingly to only track relevant data changes.
- Use the `key` attribute for lists to help Vue track changes efficiently.
- Pass only the necessary props. Avoid passing whole objects.
- Use dynamic imports and lazy-loading
- Use libraries like Vue [Virtual Scroll List](https://github.com/tangbc/vue-virtual-scroll-list) to render only the visible items in large lists.
- Use a debounce function (e.g., with lodash) for expensive operations like search or scroll events.  (e.g., `const search = debounce(()=> {search(query)}, 280)`).
- Use [`v-memo`](https://vuejs.org/api/built-in-directives.html#v-memo) to memoize large subtrees and `v-for` lists to skip unnecessary updates.
- Use `v-show` instead of `v-if` to conditionally render elements that toggle frequently.
- Avoid inline styles and animations that affect layout or trigger reflows. Use class bindings for conditional styling.

### Further reference
- https://vuejs.org/guide/best-practices/performance
