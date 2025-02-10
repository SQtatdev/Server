import socket

HOST = '0.0.0.0'
PORT = 65432       

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen(5)
print(f"Server is listening on {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    client_socket.sendall(b'Welcome to the server!')

    data = client_socket.recv(1024)
    if data:
        print(f"Received from client: {data.decode('utf-8')}")
        client_socket.sendall(b"Message received!")

    client_socket.close()
