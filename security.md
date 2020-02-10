# Security

### Question
Explain subresource integrity?

### Answer
The subresource integrity is a security feature that allows the browser to verify the resource being fetched has not been manipulated.

The integrity feature specifies a base-64 ecrypted hash of the resource being fetched. 

```html
<script integrity="{{base-64}}"></script>
```

---

### Question
What is the difference betwen cross-site scripting and cross-site request forgery?

### Answer
Cross-site scripting (XSS) is a web vunerability that allows attackers to inject client-side scripts into web pages viewed by the user. Cross-site request forgery (CSRF or XSRF) is a vunerability that induces users to perform an action unintentionally (ex.  attackers bypassing same origin policy). 

---

### Question
What is `Content Security Policy`?

### Answer

Content Security Policy (CSP) help mitigates attacks such as XXS and data injection by enabling the browser to know which domains are valid sources of executable scripts.

---

### Question
What is the difference between HTTP and HTTPS

### Answer
HTTP operated on port 80 where as HTTPS operates on port 443. While HTTP transfers data as plain text, HTTPS transfers data as encrypted text. HTTPS requires a valid SSL certificate issued by a certificate authority (CA). 



