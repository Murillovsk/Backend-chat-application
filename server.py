from email.header import Header
import threading
import socket


clients = []


def handle_client(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            remove_client(client)
            break


def broadcast(msg, client):
    for client in clients:
        if client != Header:
            try:
                client.send(msg)
            except:
                remove_client(client)


def remove_client(client):
    clients.remove(client)


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Started the chat server")

    try:
        server.bind(("localhost", 7777))
        server.listen()
    except:
        return print('\nUnable to start server\n')
    
    while True:
        client, addr = server.accept()
        clients.append(client)
        print(f'Client connected successfully. IP: {addr}')

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


main()
