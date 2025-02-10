import asyncio

HOST = '0.0.0.0'
PORT = 65432

async def handle_client(reader, writer):
    """Асинхронная обработка клиента."""
    addr = writer.get_extra_info('peername')
    print(f"Подключение от {addr}")

    writer.write(b'Welcome to the server!\n')
    await writer.drain()  # Ждем, пока данные отправятся

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break
            print(f"Получено от {addr}: {data.decode().strip()}")
            writer.write(b"Message received!\n")
            await writer.drain()
    except asyncio.CancelledError:
        print(f"Соединение с {addr} принудительно закрыто.")
    finally:
        writer.close()
        await writer.wait_closed()
        print(f"Соединение с {addr} завершено.")

async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    addr = server.sockets[0].getsockname()
    print(f"Сервер запущен на {addr}")

    async with server:
        await server.serve_forever()

asyncio.run(main())
