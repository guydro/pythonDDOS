The followoing are instructions for setting up the DDOS system:

To set up the c&c server on a new machine:
	A. Copy the "c&c server" folder to the desired computer.
	B. On "launch_attck.py" and "commandAndControl.py":
		1. Change the HOST parameter to your computers ip (static ip is recommended).
		2. Change the PORT parameter to the parameter you wish to use for your server.



	To set up a new client (aka 'infected computet'):
	A. Copy the "client" folder to the desired computer.
	B. On "virusServer.py":
		1. Change the PORT parameter to the parameter you wish to use for your client.
		2. Change the server_host and server_port to the c&c's HOST and PORT parameters respectively.
	C. Set the "number_of_logical_processors" parameter to the number of logical processors you want the client to allocate to an attack.

To launch an attack:
	A. Activate the c&c server by running "commandAndControl.py"
	B. On each client, run "virusServer.py" 
	C. On "attack_variables.txt" change the variables as you wish in the following format:
		"target's_ip_address" attack_duration "spoofed_origin_ip_address" batch_size data_per_packet
	Where:
		target's_ip_address is the ip of the attack's target.
		attack_duration is the duration of the attack in seconds.
		spoofed_origin_ip_address is the ip address that the attack's target will try to respond to.
		batch_size is not very relevant and should be kept at 1000, it is the number of packets sent in each iteration of the attack's while loop in "virusDNA.py".
		data_per_packet is the extra data in each packet (in Bytes).
	
	D. run "launch_attack.py" (note that the order of A, B and C can be interchanged, but make sure all clients are registered on the c&c server before step D).

Restrictions of program:
1. By design the program can't run indefinitely, but there is no limit to the attack_duration variable.
2. A lot of networks have DDOS protection that can easily detect and block the attack.
3. The code is not designed to work outside of a LAN.

Note: for the project to work, the scapy module has to be installed.