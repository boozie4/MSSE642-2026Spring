# Assignment 1: Cross-Site Scripting (XSS)

## Overview

This assignment explains what cross-site scripting is, how it works, and how to prevent this type of attach. 

## What is XSS?

Cross-Site Scripting is a security vulnerability that allows an attacker to inject malicious sripts into web pages. When these are viewed by other people, the script is executed, potentially allowing the attacher to:

- Steal session cookies or tokens
- Steal user login information
- Redirect the user to a malicious website
- Impersonate a user
- Modify a web page

## Exercises

### 1. Vulnerable Application

A vulnerable guestbook application was created using Replit to demonstrate and test cross-site scripting attacks.

https://xss-showcase--eboozell4.replit.app/vulnerable

This vulnerable guestbook application demo allows the user to test different scripts to see how they affect the web application.

### 2. Secure Application

A secure guestbook application was created using Replit to demonstrate and test cross-site scripting attacks against an application that is coded properly to defend against these types of attacks.

https://xss-showcase--eboozell4.replit.app/secure

## Key Differences

### Vulnerable Version

The vulnarable guestbook uses the React property "dangerouslySetInnerHTML". This property tells the browser to interpret saved strings as HTML. So, if the user submits a script, "<script>alert('Hacked')</script>", the browser sees a script tag and executes the code.

### Secure Version

The secure guestbook uses the React data binding ({comment.content}). This causes React to automatically escape the content and convert characters like "<" and ">" into HTML entities. The browser then treats the input as literal text rather than as executable code.

## Best Practices to Prevent XSS

1. Output encoding
- Escape HTML
- JavaScript string encoding
- URL encoding
- Escape CSS
2. Validate and Sanitize input
<u>Validation</u>
- Only allow expected characters
- Set and enforce length limits
- Utilize allow lists opposed to block lists
<u>Sanitize</u>
- DOMPurify
- OWASP Java HTML Sanitizer
3. Use Content Security Policy
- Strong content security policy can reduce damage even if cross-site scripting does occur.
4. Only use modern frameworks and use them correctly
- Frameworks only help if they are used safely
- Follow security guidelines from frameworks
5. Keep dependencies updated
- Monitor CVEs
- Keep plugins updated
- Patch frameworks when available
6. Regularly perform security testing
- Pen Testing
- Automated scanners
- Review code