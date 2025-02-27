import socket
import threading

clients = []

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 7777))
        server.listen() # Quantidade de conexões
    except:
        return print('Erro ao iniciar o servidor')

    while True:
        client, addr = server.accept()
        clients.append(client)

        t1 = threading.Thread(target=messagesTreatment, args=[client])
        t1.start()


def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcastMessages(msg, client)
        except:
            deleteClient(client)
            break

def broadcastMessages(msg, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)

def deleteClient(client):
    clients.remove(client)

main()