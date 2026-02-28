# Assignment 2: Cryptographic Failure

## Overview

This assignment explains what cryptographic failures are, how they work, and how to mitigate them and prevent them.

## What is Cryptographic Failure?

Cryptographic failures are security weaknesses that occur when encryption or cryptographic protections are improperly implemented or missing all together. A cryptographic failure can occur because of one of the following:

- Weak or outdated algoriths being used
- Sensitive data is not encrypted correctly
- Encryptions keys are poorly managed

Some common cryptographic failures include:

- Data transmitted without encryption
- Weak cryptographic algorithms
- Improper password storage
- Poor encryption key management
- Broken random number generation
- Improper encryption modes
- Sensitive data stored incorrectly or unnecessarily

## Exercises

### 1. Vulnerable Application

A vulnerable dashboard application was created using Replit to demonstrate and test cryptographic failures.

https://crypto-vulnerability-demo.replit.app/vulnerable

In this demo, you can toggle the protection method and type in some text that is considered sensitive. Once stored, the demo demonstrates how the data is captured and still able to be read in plain text.

### 2. Secure Application

A secure dashboard application was created using Replit to demonstrate and test proper protection against cryptographic failures.

https://crypto-vulnerability-demo.replit.app/secure

In this demo, the encryption algorithm is set automatically to AES-256-GCM and cannot be changed. Additionally, the key size is set to 256 bits and cannot be changed. The user is able to enter text that is considered sensitive. Once submitted to the database, the user can try to decrpyt the data. However, they are denied with a pop-up that says "Access Denied / Key Required". Because the user does not have the client side key, they are unable to decrypt the sensitive data that was encrypted.

## Key Differences

### Vulnerable Version

- Plaintest Storage - Messages saved as plaintext are stored exactly how they are typed in. Anyone who is able to access the database has the ability to read messages stored in plaintext.
- ROT13 - This is a simple letter-substitution cipher that shifts each letter by 13 positions. 
- Base64 - This is encoding, not encryption. Base64 is designed to represent binary data as text. It is not intended to be used to protect data.
- No Key Management - Non of the above methods mentioned uses a secret key. This means there is nothing preventing anyone from being able to read the data.

### Secure Version

- AES--256-GCM Encryption - An industry-standard algorithm. Banks and governments use this algorithm. The ciphertext is completely meaningless unless the user has the correct secret key. 
- Initialization Vector - This involves generating a random value for every single message. Utilizing this would mean that encrypting the same text more than once would produce completely different ciphertext each time. This prevents bad actors from being able to analyze and determine a pattern.
- Authentication Tag - This is a tamper-detection mechanism that is built into GCM mode. If a bad actor modifies any of the ciphertext, decryption fails and the person who encrypted the text is notified of tampering.
- Server-Side Decryption Only - With this method, the secret key never leaves the server. In order to decrypt any text, a request to the backend is required, simulating proper access control.

## Best Practices to Prevent Cryptographic Failures

1. Use updated and strong encryption algorithms

- AES-256
- RSA-2048 or higher
- SHA-256 or SHA-3

2. Encrypt sensitive data at rest

- Full disk encryption
- Encrypted databases
- File encryption

3. Encrypt data being transmitted

- Use HTTPS everywhere
- Use secure APIs
- Use VPN tunnels where necessary
- Disable plaintext FTP
- Disable Telnet

4. Proper key management

- Store keys separately from the encrypted data
- Make sure keys are rotated regularly
- Restrict key access utilizing least priviledge

5. Use secure protocols only

- HTTPS
- SFTP
- SSH

6. Follow security standards

- NIST guidelines
- OWASP
- ISO 27001
