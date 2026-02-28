# Secure Software Development Lifecycle and Threat Model

## Part 1: Secure Design Document Overview

### High‑Level Project Description

The Hiking Club Application is a web‑based event management and membership platform designed
for outdoor recreation organizations. The system enables hiking clubs to publish trips,
manage registrations, collect payments, and track participants.

### Organization Description

The organization is a hiking club that manages outdoor events and maintains member records.
Sensitive data includes personal information, medical notes, and payment records.

### Deployment Environment

The system is deployed in a cloud‑hosted environment with a front‑end web server located in a
DMZ and a backend database server located in a private subnet. Firewalls separate network
segments.

### System Assets

- Member personal information
- Medical information
- User credentials
- Payment records
- Administrative accounts
- Database contents
- System logs

## Part 2: STRIDE Threat Model

| Category               | Example Threat                |
| ---------------------- | ----------------------------- |
| Spoofing               | Stolen credentials            |
| Tampering              | Database modification         |
| Repudiation            | Users deny actions            |
| Information Disclosure | Medical data exposure         |
| Denial of Service      | Traffic flooding              |
| Elevation of Privilege | Unauthorized admin access     |

### OWASP Top 10 Threats

- A01 Broken Access Control
- A02 Cryptographic Failures
- A03 Injection
- A04 Insecure Design
- A05 Security Misconfiguration
- A06 Vulnerable Components
- A07 Authentication Failures
- A08 Integrity Failures
- A09 Logging Failures
