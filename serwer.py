#! /usr/bin/env python
import socket
from threading import Thread, Lock

global HOST, PORT, CONNECTION_LIST, RECV_BUFFER
HOST = 'localhost'
PORT = 8888#50002
CONNECTION_LIST = []
RECV_BUFFER = 2048


class Client():
    def __init__(self, conn, name):
        self.conn = conn
        self.name = name

    def send(self, message):
        self.conn.send(message)

    def recv(self):
        return self.conn.recv(RECV_BUFFER)

    def close(self):
        self.conn.close()


def get_client(name):
    for client in CONNECTION_LIST:
        if client.name == name:
            return client
    return None


def broadcast_data(data, lock):
    lock.acquire()
    for cl in CONNECTION_LIST:
        print data
        cl.send(data)
    lock.release()


def handle_client(client, lock):                    # Obsluga klienta.
    while True:
        data = client.recv()
        if not data or data == "q":
            break
        else:
            response = str(data)

        broadcast_data(response, lock)

    #Rozlaczanie klienta.
    lock.acquire()                                   # Uzyskuje blokade na obiekcie.
    CONNECTION_LIST.remove(client)
    client.close()
    print "User " + client.name + " disconnected!"
    lock.release()                                   # Zwolnienie blokady.


def handle_server(server_socket, lock):              # Obsluga serwera.
    while True:
        conn, addr = server_socket.accept()
        print "New connection from " + str(addr)
        name = conn.recv(RECV_BUFFER)
        print "Received name: " + name
        client = get_client(name)                    # Jezeli istnieje juz gracz o takim imieniu - zakoncz polaczenie
        if client:
            conn.send('0')
            conn.close()
            print "User exists! Terminating connection " + str(addr) + " !"
        else:
            conn.send('1')
            client = Client(conn, name)
            CONNECTION_LIST.append(client)
            print "User connected!"
            response = "User %s joined the game!" % name
            length = str(len(CONNECTION_LIST))
            response += "\nCurrently %s users in chat room!" % length
            broadcast_data(response, lock)
            Thread(target=handle_client, args=(client, lock)).start()


def start_server():
    global HOST, PORT
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            server_socket.bind((HOST, PORT))
        except socket.error:
            PORT += 1
            if PORT > 9999:
                print 'Could not start TCP/IP server, sorry!'
                return
        else:
            break

    server_socket.listen(10)
    print "*****************************************"
    print "TCP/IP chat (game) server listening on port " + str(PORT)
    print "*****************************************"
    lock = Lock()
    handle_server(server_socket, lock)


if __name__ == '__main__':
    start_server()