import threading
import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 7777))
    except:
        return print('\nUnable to connect to server\n')

    username = input('User>')
    print('\nConnected')

    # Iniciar uma thread para receber mensagens
    thread_receive = threading.Thread(target=receiveMessages, args=[client])
    # Iniciar uma thread para enviar mensagens
    thread_send = threading.Thread(target=sendMessages, args=[client, username])

    thread_receive.start()
    thread_send.start()

def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg+'\n')
        except:
            print('\nUnable to stay connected to the server!\n')
            print('Press <Enter> To continue...')
            client.close()
            break

def sendMessages(client, username):
    while True:
        try:
            msg = input('\n')
            client.send(f'<{username}>{msg}'.encode('utf-8'))
        except:
            return

main()
