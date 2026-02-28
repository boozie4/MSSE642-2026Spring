# Assignment 3: Kali Linux and Metasploitable Test

## Overview

This assignment is meant to demonstrate how to successfully set up a penetration testing environment using Kali Linux and Metasploitable 2 running on VM's. The penetration testing environment being demonstrated is configured to properly utilize ethical hacking practices safely.

## Objectives

Objectives for this assignment include the following:

- Ensure the pentration testing environment is set up correctly and there is network connectivity between Kali Linux and Metasplotable 2
- Perform a basic portscan of the Metasploitable 2 system
-Answer questions and document findings

## Deliverables

### 1. Kali Linux and Metasplotable 2 Running with Confirmed Network Connectivity

![Kali and Metasploitable 2](<Assignment 3 Images/Assignment3_Image1.png>)

### 2. Metasploit Running on the Kali Linux System

![Metasploit Running](<Assignment 3 Images/Assignment3_Image2.png>)

### 3. Available Portscanners on Metasploit

![Available Portscanners](<Assignment 3 Images/Assignment3_Image3.png>)

### 4. Portscan Configuration

![Portscan Configurtion](<Assignment 3 Images/Assignment3_Image4.png>)

### 5. Port Scan Findings

![Portscan Findings](<Assignment 3 Images/Assignment3_Image5.png>)

**Analysis:**

Metaploit was configured to scan only ports 1 through 1024. With this configuration, port 22 (SSH) was found to be open on the Metasploitable 2 system. Metasploitable 2 is meant to be used to perform pentesting techniques on. Because of this, this system with Kali Linux and Metasploitable 2 running on VM's configured on the same network makes for the perfect pentesting lab where everything can be done in a safe and controlled environment. 

## Questions

### What is the purpose of port scanning from the perspective of a Black Hat hacker?

- From the perspective of a Black Hat hacker, port scanning is used as a method of reconnaissance. Running a port scan can provide the following information:

- - Which ports are open
- - Which ports are closed
- - Which ports are filtered by a firewall

When performing the port scan, some of the target ports a hacker may be searching for include the following:

- Port 22 (SSH)
- Port 80 (HTTP)
- Port 443 (HTTPS)
- Port 3389 (Remote Desktop)
- Port 21 (FTP)

When a port is labeled as open, it can be a potential point of attach for a hacker.

### What is the purpose of port scanning from the perspective of an Ethical (White Hat) hacker?

- When performing port scans, White Hat hackers are looking for the same information as Black Hat hackers. However, the reason for finding this information for White Hat hackers is so they can identify security weakensses so they can be patched and fixed before any bad actors exploit them.

### Why did we restrict the scanned ports to 1 thorugh 1024?

- Ports 1 through 1024 are known as "well-known ports". Some of the common ports in this range include the following:
-- Port 21 (FTP)
-- Port 22 (SSH)
-- Port 25 (SMTP)
-- Port 53 (DNS)
-- Port 80 (HTTP)
-- Port 110 (POP3)
-- Port 143 (IMAP)
-- Port 443 (HTTPS)

These ports tend to run core network serices, making them common targets for hackers. Limiting the scanned ports to 1 through 1024 makes the portscan fast but efficient, making this technique still useful for cybersecurity analysis.