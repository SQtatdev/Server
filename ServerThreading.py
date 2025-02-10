import socket
import threading

HOST = '0.0.0.0'
PORT = 65432

def handle_client(client_socket, client_address):
    """Функция для обработки клиента в отдельном потоке."""
    print(f"Подключение от {client_address}")

    client_socket.sendall(b'Welcome to the server!')

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Получено от {client_address}: {data.decode('utf-8')}")
            client_socket.sendall(b"Message received!")
    except ConnectionResetError:
        print(f"Клиент {client_address} отключился принудительно.")
    finally:
        client_socket.close()
        print(f"Соединение с {client_address} закрыто.")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Сервер запущен на {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
