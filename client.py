import socket
import threading


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 7777))
    except:
        return print('Erro ao conectar ao servidor')

    username = input('Username: ')
    print('conectado')

    t1 = threading.Thread(target=receiveMessages, args=[client])
    t2 = threading.Thread(target=sendMessages, args=[client, username])

    t1.start()
    t2.start()


def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg)
        except:
            print('Não foi possivel permanecer conectado ao servidor')
            print('Precione <Enter> para continuar...')
            client.close()
            break


def sendMessages(client, username):
    while True:
        try:
            msg = input('')
            client.send(f'<{username}> diz: {msg}'.encode('utf-8'))
        except:
            return


main()