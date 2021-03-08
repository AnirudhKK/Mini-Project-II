#!/usr/bin/env python3

import subprocess
import optparse
import re

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface name to change MAC Address for")
    parser.add_option("-m", "--mac", dest="new_mac_address", help="New MAC address you want")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use -h or --help for more info.")
    elif not options.new_mac_address:
        parser.error("[-] Please specify a new MAC address you want, use -h or --help for more info.")

    if re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", options.new_mac_address):
        return options
    else:
        parser.error("[-] Not a valid MAC address! Try again with a valid MAC address")

def change_mac(interface, new_mac_address):
    print("[+] Changing MAC address for "+interface+" to "+new_mac_address)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac_address])
    subprocess.call(["ifconfig",interface,"up"])

def get_mac(interface):
    new_ifconfig_output = subprocess.check_output(["ifconfig", interface])
    mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(new_ifconfig_output))
    if mac_address:
        return mac_address.group(0)
    else:
        return None

#---------------------- MAIN------------------------------------------

options = get_argument()

change_mac(options.interface, options.new_mac_address)

new_mac = get_mac(options.interface)

if new_mac == options.new_mac_address:
    print("[+] MAC address changed to "+new_mac)
else:  
    print("[-] Encountered an error while changing MAC address!")
