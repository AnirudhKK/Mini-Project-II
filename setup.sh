printf "______________.___._______________________________            _____________________________  
\_   ___ \__  |   |\______   \_   _____/\______   \          /   _____/\_   _____/\_   ___ \ 
/    \  \//   |   | |    |  _/|    __)_  |       _/  ______  \_____  \  |    __)_ /    \  \/ 
\     \___\____   | |    |   \|        \ |    |   \ /_____/  /        \ |        \\\\     \____
 \______  / ______| |______  /_______  / |____|_  /         /_______  //_______  / \______  /
        \/\/               \/        \/         \/                  \/         \/         \/ "
echo "\nInstalling. Have patience\n"
sudo apt-get install -y python3 > /dev/null 2>&1
sudo apt install -y python3-pip > /dev/null 2>&1
echo "\nInstalling.. Have patience\n"

pip3 install scapy > /dev/null 2>&1
echo "\nInstalling... Have patience\n"
pip3 install scapy_http > /dev/null 2>&1
echo "\nInstalling.... Have patience\n"
pip3 install requests > /dev/null 2>&1

sudo chmod +x mac_changer.py
sudo chmod +x network_scanner.py
sudo chmod +x arp_spoofer.py
sudo chmod +x crawler.py
sudo chmod +x spider.py
sudo chmod +x extract_wifi_pass.py

sudo cp mac_changer.py /bin/mac_changer
sudo cp network_scanner.py /bin/network_scanner
sudo cp arp_spoofer.py /bin/arp_spoofer
sudo cp crawler.py /bin/crawler
sudo cp spider.py /bin/spider
sudo cp extract_wifi_pass.py /bin/extract_wifi_pass

printf "\nTools have been installed successfully. They can be accessed by following commands :- "
printf "\n1. MAC Changer              -  mac_changer [arguments]"
printf "\n2. Network Scanner          -  network_scanner [arguments]"
printf "\n3. Crawler                  -  crawler [arguments]"
printf "\n4. Spider                   -  spider [arguments]"
printf "\n5. Wifi-Pass Extractor      -  extract_wifi_pass"
