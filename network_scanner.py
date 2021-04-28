#!/usr/bin/env python3

import scapy.all as scapy
import argparse

def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--target", dest="target", help="Target IP address/range")
	options = parser.parse_args()
	if not options.target:
		parser.error("[-] Please specify target IP/range, use -h or --help for more info.")
	return options

def scan(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answered_packets = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
	
	clients_list = []
	
	for element in answered_packets:
		client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}
		clients_list.append(client_dict)
	return clients_list
	
def print_result(results_list):
	print("IP\t\t\tMAC ADDRESS\n-------------------------------------------------------")
	for client in results_list:
		print(client["ip"]+"\t\t"+client["mac"])

# ----------------------- MAIN -----------------

print(""" _______          __                       __       _________                                         
 \      \   _____/  |___  _  _____________|  | __  /   _____/ ____ _____    ____   ____   ___________ 
 /   |   \_/ __ \   __\ \/ \/ /  _ \_  __ \  |/ /  \_____  \_/ ___\\\\__  \  /    \ /    \_/ __ \_  __ \\
/    |    \  ___/|  |  \     (  <_> )  | \/    <   /        \  \___ / __ \|   |  \   |  \  ___/|  | \/
\____|__  /\___  >__|   \/\_/ \____/|__|  |__|_ \ /_______  /\___  >____  /___|  /___|  /\___  >__|   
        \/     \/                              \/         \/     \/     \/     \/     \/     \/       """)

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)