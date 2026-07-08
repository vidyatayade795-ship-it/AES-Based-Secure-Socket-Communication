# AES-Based Secure Socket Communication

## Overview

This project is a Python-based client-server communication system designed to demonstrate secure communication over a Local Area Network (LAN). The application uses TCP sockets on port 5000 to establish a connection between a client and a server. To ensure data confidentiality, all messages are encrypted using the Advanced Encryption Standard (AES) before transmission and decrypted upon receipt. The project was developed and tested on Kali Linux and provides a practical understanding of networking, socket programming, and cryptography.

## Features

- Client-server communication using TCP sockets
- Secure message transmission with AES encryption
- Communication over port 5000
- Real-time data exchange within a Local Area Network
- Developed and tested on Kali Linux
- Simple and modular Python implementation

## Technologies Used

- Python 3
- Socket Programming
- TCP/IP Protocol
- AES Encryption
- Kali Linux

## Project Structure

```
AES-Based-Secure-Socket-Communication/
│── client.py
│── server.py
│── README.md
```

## Installation

1. Clone the repository.

```bash
git clone https://github.com/your-username/AES-Based-Secure-Socket-Communication.git
```

2. Navigate to the project directory.

```bash
cd AES-Based-Secure-Socket-Communication
```

3. Install the required dependencies.

```bash
pip install pycryptodome
```

## Usage

Start the server:

```bash
python3 server.py
```

The server listens for incoming connections on port **5000**.

In another terminal or on another device connected to the same network, start the client:

```bash
python3 client.py
```

Enter the server's IP address if required and begin exchanging encrypted messages.

## Working

The server waits for incoming TCP connections on port 5000. Once a client connects, messages are encrypted using AES before being transmitted across the network. The receiving end decrypts the messages using the same encryption key, allowing secure communication between the client and server.

## Learning Outcomes

This project helped strengthen my understanding of:

- Socket Programming
- TCP/IP Networking
- Client-Server Architecture
- AES Encryption
- Secure Network Communication
- Python Application Development

## Future Enhancements

- Multi-client support
- Secure key exchange mechanism
- Graphical user interface
- File transfer functionality
- SSL/TLS implementation
- User authentication

## Author

**Vidya Tayade**
