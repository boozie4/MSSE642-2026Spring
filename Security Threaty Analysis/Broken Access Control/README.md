# Assignment 2: Cryptographic Failure

## Overview

This assignment explains what Broken Access Control is, how it can cause security concerns, and what steps to take in order to mitigate it.

## What is Broken Access Control?

Broken Access Control is a security vulnerability in which the system fails to properly restrict what actions users are allowed to perform and what data and information users are allowed to access. Broken Access Control is considered one of the most critical vulnerabilities and is very often ranked as number 1 in the OWASP top 10 because it can expose sensitive information and data and it can leave systems open to attackers.

## Exercises

### 1. Vulnerable Application

A vulnerable application was created using Replit that can be used to demonstrate and explore how Broken Access Control works. 

https://access-control-demo.replit.app/vulnerable

In this demo, the user logs in. Once logged in, when they attempt to gain access to another users account and information, the API being used only confirms that the user is logged in. It does not verify that the requested user ID belongs to the session in use. Because of this, any authenticated user is able to view anyone else's private data.

### 2. Secure Application

A secure application was created using Replit that can be used to demonstate how systems work when proper access control is enforced. 

https://access-control-demo.replit.app/secure

In this demo, once logged in, if the user attempts tp gain access to another users private data, the API verifies if the user's session ID matches the requested resource ID. If it matches, the user is allowed to access the requested data. If it does not match, the system returns 403 Forbidden.

## Key Differences

### Vulnerable Version

- Only verifies that the user is logged in
- Does NOT check who is making the request
- Returns any user's private data when requested as long as the requester has a valid session
- Any logged in user can simply change the ID in the URL so they are able to access someone else's private data. This data can include SSN, salary, private internal notes, etc.

### Secure Version

- Verifies that the user is logged in AND that any requested resources belongs to the requester. 
- Compares the session's user ID to the requested data ID
- If session ID's do not match, the system returns 403 Forbidden and access is denied
- Authenticated users are only able to access their own data

## Best Practices to Prevent Broken Access Control

1. Deny access by default
2. Enforce access control on servers

Never trust the frontend. Attackers are able to bybass the following: 

- Buttons
- Hidden fields
- JavaScript
- Disabled controls.

3. Used role-based access control (RBAC)

Define roles like the following:

- Admin
- Manager
- User
- Guest

4. Validate object ownership

Users should only be allowed to access their own data.

5. Use strong session management

Requirements include:

- Secure cookies
- Session timeouts
- Regenerate session IDs
- Use HTTPS only

Examples of secure settings include:

- HttpOnly
- Secure
- SameSite=Strict

6. Avoid predictable IDs

Sequential IDs are easy to guess. Use the following instead:

- UUIDs
- Random tokens

7. Centralize access control logic

Avoid scattered permission checks. Benefits include:

- Easier audits
- Fewer mistakes
- Cleaner code

8. Log and monitor access attempts

This helps to detects attempted attacks early. Items that should be tracked include:

- Failed logins
- Unauthorized access attempts
- Admin actions

9. Rate limit sensitive actions

This can help to prevent automated attacks. Items that should be rate limited include:

- Login attempts
- Password resets
- Account lookups

10. Test access control regularly

- Manual testing
- Automated scanners
- Penetration testing

11. Use the principle of least privilege

Users should only have the permissions required to accomplish their own duties