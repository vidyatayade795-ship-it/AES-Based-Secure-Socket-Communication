import socket
from cryptography.fernet import Fernet

KEY=b'F7StOlYUufcTuWWEEbPNmge_TD65BFvRzcJLNq1LZs8='
cipher=Fernet(KEY)

SERVER_IP=input("Enter Server IP:")

PORT=5000

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((SERVER_IP,PORT))

print("\n Connected Successfully!")
print("Type 'exit' to quit \n")

while True:
    message =input("Hello vidya:")

    if message.lower()=="exit":
        break
 
  
        encrypted=cipher.encrypt(message.encode())
        print("\n Encrypted Message:")
        print(encrypted)
 
        client.send(encrypted)
client.close()
