#!/usr/bin/env python3

from platform import system
import subprocess, re

def get_os():
    return system()

def get_linux_wifi():
    files = subprocess.check_output("cd /etc/NetworkManager/system-connections/ && ls -a", shell=True)
    files = str(files, 'utf-8').split("\n")
    files = files[2:-1]
    for file in files:
	    file_details = subprocess.check_output("cd /etc/NetworkManager/system-connections/ && cat \""+file+"\"",  shell=True)
	    file_details = str(file_details, 'utf-8')
	    if 'type=wifi' in file_details:	
		    ssid = re.search("(?:ssid=)(.*)", file_details)[1]
		    ssid_password = re.search("(?:psk=)(.*)", file_details)[1]
		    if ssid:
			    print("-----------------------\nName = "+ssid+"\nPassword = "+ssid_password)

def extract_network_names():
    get_networks_command = "netsh wlan show profile"
    networks = subprocess.check_output(get_networks_command, shell=True)
    network_names_list = re.findall("(?:Profile\s*:\s)(.*)", str(networks, 'utf-8'))
    return network_names_list

def extract_password_network(network):
    get_password_command = "netsh wlan show profile \"" + network + "\" key=clear"
    result = subprocess.check_output(get_password_command, shell=True)
    password = re.findall("(?:Key Content\s*:\s)(.*)", str(result, 'utf-8'))
    if password:
        return password[0]
    else:
        return "----------NO PASSWORD----------"

print("""

 __      __.______________.___         __________  _____    _________ _________
/  \    /  \   \_   _____/|   |        \______   \/  _  \  /   _____//   _____/
\   \/\/   /   ||    __)  |   |  ______ |     ___/  /_\  \ \_____  \ \_____  \ 
 \        /|   ||     \   |   | /_____/ |    |  /    |    \/        \/        \\
  \__/\  / |___|\___  /   |___|         |____|  \____|__  /_______  /_______  /
       \/           \/                                  \/        \/        \/ 

""")

os = get_os()
if(os == 'Windows'):
    network_names = extract_network_names()
    for name in network_names:
        print("----------------------------------------------------\nWifi Name = " + name +"\nPassword = "+ extract_password_network(str(name)))
elif(os == 'Linux'):
    get_linux_wifi()