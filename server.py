import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 65431
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print("Server of Gezhagn")


def clients(connection, address):
    while True:
        name = connection.recv(1024)
        print(name.decode())
        connection.sendall("server Gezhagn".encode())
        data = connection.recv(1024)
        if not data:
            break
        number = int(data.decode())

        server_number = input("Enter a server_number between 1 and 100: ")
        if server_number.isdigit() and 1 <= int(server_number) <= 100:
            print(f"client number: {number}")
            connection.sendall(server_number.encode())
            print(f"server number: {server_number}")
            result = number + int(server_number)
            connection.sendall(str(result).encode())

            print(f"sum of the numbers : {result}")

    connection.close()


for i in range(2):
    connection, address = server.accept()
    print(f"Connected by {address}")
    threading.Thread(target=clients, args=(connection, address)).start()
