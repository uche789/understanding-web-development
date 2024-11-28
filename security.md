# Security

## Subresource integrity?

The subresource integrity is a security feature that allows the browser to verify the resource being fetched has not been manipulated.

The integrity feature specifies a base-64 ecrypted hash of the resource being fetched. 

```html
<script integrity="{{base-64}}"></script>
```

## Difference betwen cross-site scripting and cross-site request forgery

Cross-site scripting (XSS) is a web vunerability that allows attackers to inject client-side scripts into web pages viewed by the user. Cross-site request forgery (CSRF or XSRF) is a vunerability that induces users to perform an action unintentionally (ex.  attackers bypassing same origin policy). 

### CSRF token

CSRF tokens are used to verify that the user sending the request is legitimate. They are essential for requests that modify the state on the server.

#### Resources
- https://owasp.org/www-community/attacks/csrf
- https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html

## Content Security Policy (CSP)

Content Security Policy help mitigates attacks such as XXS and data injection by enabling the browser to know which domains are valid sources of executable scripts.

## DDoS (Distributed Denial-of-Service)

Distributed Denial-of-Service (DDoS) is a cyber-attack where an attacker floods a server with internet traffic, prevent the server to be used for its intended purpose and denying user access to connecting online services and sites.

Race conditions can be exploited to perform DDoS attacks. In such cases, an attacker deliberately triggers a race condition to create a deadlock, exhausting computing resources and rendering the service unavailable.

### Further reading(s)

[Five Most Famous DDoS Attacks and Then Some](https://www.a10networks.com/blog/5-most-famous-ddos-attacks) 



