import socket
from cryptography.fernet import Fernet

Key = b'F7StOlYUufcTuWWEEbPNmge_TD65BFvRzcJLNq1LZs8='
cipher = Fernet(Key)

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen(100)
print("="*50)
print("Secure Chat Server Started")
print("="*50)

print(f"Listening on Port {PORT}....")
print("Waiting for Client...\n")
client,address = server.accept()
print(f"Client Connected{address}\n")
while True:
	encrypted = client.recv(4096)
	if not encrypted:
		break
	print("Encrypted Data Received:")
	print(encrypted)
    
	try:
		message = cipher.decrypt(encrypted).decode()
       
		print("\nDecrpyted Message:")
		print(message)
		print("-"*50)
	except Exception:
		print("Unable to decrypt message.")
client.close()
server.close()
