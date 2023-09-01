import toolbox
import socket
import threading
import requests

# Function that gets the public IP address
def get_public_ip_address():
    try:
        # Send an HTTP GET request to a service that echoes your public IP address
        response = requests.get("https://httpbin.org/ip")
        
        # Parse the JSON response to extract the public IP address
        public_ip_address = response.json()["origin"]
        
        return public_ip_address
    except Exception as e:
        return str(e)

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

    # We get the public IP address
    public_ip = get_public_ip_address()
    if public_ip:
        print(f"Your public IP address is: {public_ip}")
    else:
        print("Failed to retrieve public IP address.")

    print(f"Server listening on {server_host}:{server_port}")
    print(f"Server IP address: {public_ip}")

    while True:
        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
        
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
