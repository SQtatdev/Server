import socket

server_ip = '192.168.0.23'
server_port = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

while True:
    message = input("enter message, exit to quit")
    client_socket.send(message.encode())
    if message.lower() == "exit":
        break
client_socket.close()



