# Security

## Subresource integrity?

The subresource integrity is a security feature that allows the browser to verify the resource being fetched has not been manipulated.

The integrity feature specifies a base-64 ecrypted hash of the resource being fetched. 

```html
<script integrity="{{base-64}}"></script>
```

---

## Difference betwen cross-site scripting and cross-site request forgery

Cross-site scripting (XSS) is a web vunerability that allows attackers to inject client-side scripts into web pages viewed by the user. Cross-site request forgery (CSRF or XSRF) is a vunerability that induces users to perform an action unintentionally (ex.  attackers bypassing same origin policy). 

---

## Content Security Policy (CSP)

Content Security Policy help mitigates attacks such as XXS and data injection by enabling the browser to know which domains are valid sources of executable scripts.




