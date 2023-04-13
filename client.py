import socket

HOST = "192.168.337.26"
PORT = 65432
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))
print("connected to server ")
# socket.gethostbyname(socket.gethostname())

while True:
    server.sendall("Client of abela".encode())
    Client_number = input("Enter a Client_number between 1 and 100: ")
    if Client_number.isdigit() and 1 <= int(Client_number) <= 100:
        print(f"My 23number is :{Client_number}")
        server.sendall(Client_number.encode())

        name = server.recv(1024).decode()
        print(f"server name : {name}")
        server_number = server.recv(1024).decode()
        print(f"The server number is: {server_number}")
        result = server.recv(1024).decode()
        print(f"The result is :{int(result)}")
        # result=int(server_number)+int(Client_number)
        # print(f'The result is: {result}')

        break
    else:
        print("Invalid input.a Client_number must be between 1 and 100.")
        print("connection is break")
        break
