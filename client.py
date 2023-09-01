import socket
import toolbox

def main():
    server_host = "127.0.0.1"
    server_port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_host, server_port))

    # We send info about the host
    contents = toolbox.get_special_folders_contents()
    special_content = ""
    for folder_name, files in contents.items():
        special_content.join(f"{folder_name} Files:")
        for file_name in files:
            special_content.join(f"- {file_name}")
        print()
    client.send(special_content.encode('utf-8'))
    print(special_content)


    while True:
        message = input("Enter a message: ")
        if message.lower() == "exit":
            break
        client.send(message.encode('utf-8'))

    client.close()

if __name__ == "__main__":
    main()
