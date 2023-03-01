import socket

HOST = "192.168.0.153"
PORT = 8012

#connect to server
host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_socket.connect((HOST, PORT))

#send attack signal
host_socket.send(f"attack".encode("ascii"))