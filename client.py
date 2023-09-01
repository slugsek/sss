import socket

def main():
    server_host = "127.0.0.1"
    server_port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_host, server_port))

    while True:
        message = input("Enter a message: ")
        if message.lower() == "exit":
            break
        client.send(message.encode('utf-8'))

    client.close()

if __name__ == "__main__":
    main()
