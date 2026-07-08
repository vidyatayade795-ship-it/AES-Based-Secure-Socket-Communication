# AES-Based Secure Socket Communication

## Overview

AES-Based Secure Socket Communication is a Python-based networking project that demonstrates secure communication between a client and a server over a Local Area Network (LAN). The application uses TCP sockets on port **5000** to establish a connection, while the **Fernet** implementation from the `cryptography` library is used to encrypt and decrypt messages.

The project was developed and tested on **Kali Linux** as part of a cybersecurity and networking learning exercise. It demonstrates the practical implementation of socket programming, client-server architecture, TCP/IP communication, and symmetric encryption to protect data transmitted across the network.

## Features

- TCP client-server communication
- Secure message encryption using Fernet (AES-based)
- Message decryption at the server
- Communication over port 5000
- Local Area Network (LAN) communication
- Simple command-line interface
- Built using Python

## Technologies Used

- Python 3
- Socket Programming
- TCP/IP Protocol
- Cryptography (Fernet)
- Kali Linux

## Project Structure

```
AES-Based-Secure-Socket-Communication/
│── client.py
│── server.py
│── requirements.txt
│── .gitignore
│── README.md
└── screenshots/
```

## Requirements

Install the required package before running the project:

```bash
pip install -r requirements.txt
```

or

```bash
pip install cryptography
```

## How to Run

### Start the Server

```bash
python3 server.py
```

The server starts listening for incoming TCP connections on **port 5000**.

### Start the Client

```bash
python3 client.py
```

Enter the server's IP address when prompted. Ensure both devices are connected to the same Local Area Network (LAN).

## Working

1. The server starts and listens on port **5000**.
2. The client connects to the server using its IP address.
3. The client encrypts the message using **Fernet** encryption before sending it.
4. The server receives the encrypted data.
5. The server decrypts the message and displays the original plaintext.

This process demonstrates secure communication using symmetric encryption over a TCP connection.

## Screenshots
<img width="1600" height="900" alt="WhatsApp Image 2026-07-09 at 1 37 42 AM" src="https://github.com/user-attachments/assets/20bc3bec-ce16-4ea4-8475-ba285e6cad83" />
<img width="1599" height="838" alt="WhatsApp Image 2026-07-09 at 1 37 41 AM" src="https://github.com/user-attachments/assets/780a9de6-63a8-4e78-a3a4-23869e44e50b" />



## Learning Outcomes

Through this project, I gained practical experience with:

- Python socket programming
- TCP/IP networking
- Client-server architecture
- Symmetric encryption using Fernet
- Secure data transmission
- Network communication on Linux

## Future Enhancements

- Multi-client support
- Secure key management using environment variables
- User authentication
- File transfer over encrypted channels
- Graphical User Interface (GUI)
- Logging and monitoring
- SSL/TLS implementation

## Author

**Vidya Tayade**

First-Year B.Tech (Information Technology)
