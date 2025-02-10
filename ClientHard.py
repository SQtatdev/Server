import socket
import threading

server_ip = '192.168.0.23'
server_port = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_ip, server_port))
    print("✅ Подключено к серверу.")
except ConnectionRefusedError:
    print("❌ Ошибка: сервер недоступен.")
    exit()

def receive_messages():
    """Функция для получения сообщений от сервера."""
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"\n📩 Сообщение от сервера: {data.decode()}\n> ", end="")
        except ConnectionResetError:
            print("\n🚫 Соединение с сервером потеряно.")
            break
    client_socket.close()

# Запускаем поток для получения сообщений
receive_thread = threading.Thread(target=receive_messages, daemon=True)
receive_thread.start()

while True:
    message = input("> ")
    if message.lower() == "exit":
        break
    try:
        client_socket.send(message.encode())
    except BrokenPipeError:
        print("❌ Ошибка: соединение закрыто.")
        break

client_socket.close()
print("🚪 Клиент отключен.")
