import subprocess, re

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
network_names = extract_network_names()
for name in network_names:
    print("----------------------------------------------------\nWifi Name = " + name +"\nPassword = "+ extract_password_network(str(name)))