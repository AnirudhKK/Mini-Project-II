sudo apt-get install -y python3
sudo apt install -y python3-pip

pip3 install scapy
pip3 install scapy_http
pip3 install requests

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