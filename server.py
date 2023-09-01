import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")
        except:
            break
    client_socket.close()

def main():
    server_host = "127.0.0.1"
    server_port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_host, server_port))
    server.listen(5)
    print(f"Server listening on {server_host}:{server_port}")

    while True:
        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
        
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
