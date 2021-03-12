sudo apt-get install -y python3
sudo apt install -y python3-pip
apt-get install -y build-essential python-dev libnetfilter-queue-dev

pip3 install -U git+https://github.com/kti/python-netfilterqueue
pip3 install  scapy
pip3 install  scapy_http

sudo chmod +x mac_changer.py
sudo chmod +x network_scanner.py
sudo chmod +x arp_spoofer.py
sudo chmod +x dns_spoof.py

sudo cp mac_changer.py /bin/mac_changer
sudo cp network_scanner.py /bin/network_scanner
sudo cp arp_spoofer.py /bin/arp_spoofer
sudo cp dns_spoof.py /bin/dns_spoof
