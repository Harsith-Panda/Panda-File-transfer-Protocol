print("______")
print("|     |")
print("|     |")
print("|_____|")
print("|")
print("|")
print("|   ANDA   File Transfer Protocol")

import socket
s = socket.socket()
host = input(str("Please enter the host address of the sender : "))
port = 8080
s.connect((host,port))
print("Connected ... ")

filename = input(str("Please enter a filename for the incoming file : "))
file = open(filename, 'wb')
file_data = s.recv(80636120)
file.write(file_data)
file.close()
print("File has been received successfully.")
